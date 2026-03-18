import ollama
import speech_recognition as sr
import pyttsx3
import threading
import time
from emotion import detect_emotion
from memory import update_memory, get_memory

# ================== GLOBAL STATE ==================
is_speaking = False
stop_speaking = False

# ================== SPEAK (INTERRUPTIBLE & STABLE) ==================
def speak(text):
    global is_speaking, stop_speaking

    def _run():
        global is_speaking, stop_speaking
        engine = pyttsx3.init()
        engine.setProperty("rate", 170)
        is_speaking = True
        stop_speaking = False

        engine.say(text)
        engine.startLoop(False)
        while engine.isBusy():
            if stop_speaking:
                engine.stop()
                break
            engine.iterate()
            time.sleep(0.05)
        engine.endLoop()
        engine.stop()
        is_speaking = False

    print("JOE:", text)
    threading.Thread(target=_run, daemon=True).start()

# ================== LISTEN (HINGLISH + FULL SENTENCE) ==================
def listen_from_mic():
    global stop_speaking
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.4)
        try:
            audio = r.listen(
                source,
                timeout=8,            # natural pause allow
                phrase_time_limit=12  # long human sentences
            )
        except:
            return ""

    # agar JOE bol raha ho aur user bola → interrupt
    if is_speaking:
        stop_speaking = True

    try:
        # Hinglish best support
        return r.recognize_google(audio, language="en-IN")
    except:
        return ""

print("\n🎤 JOE READY")
print("➡️ Hindi + English (Hinglish)")
print("➡️ Beech me bolo to JOE chup ho jayega")
print("➡️ Natural, short replies\n")

# ================== MAIN LOOP ==================
while True:
    spoken = listen_from_mic()
    if not spoken:
        continue

    print("You said:", spoken)
    text = spoken.lower().strip()

    # EXIT
    if "exit" in text:
        speak("Theek hai, baad me milte hain.")
        break

    # ---- MEMORY + EMOTION ----
    emotion = detect_emotion(text)
    update_memory(emotion=emotion, message=text)
    mem = get_memory()

    # ---- HUMAN-LIKE SYSTEM PROMPT ----
    system_prompt = f"""
Your name is JOE.

You are NOT a robot.
You talk like a normal Indian human.

How to reply:
- Use simple Hinglish.
- Short, natural sentences.
- Friendly and calm tone.
- No AI words like "as an AI", "I am designed".
- If user pauses or speaks casually, understand intent.

User emotion: {mem['last_emotion']}

Behavior:
- Sad/tired → soft, supportive.
- Casual → casual reply.
- Keep it human, not formal.
"""

    # ---- AI CALL ----
    try:
        response = ollama.chat(
            model="mistral",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text}
            ]
        )
        reply = response["message"]["content"]
    except:
        reply = "Samajh gaya, dobara bolna."

    # ---- SPEAK ----
    speak(reply)

