# ai-chatbot-ollama
Local LLM chatbot (Ollama) with voice input/output, emotion detection &amp; persistent memory
# 🤖 AI Voice Chatbot (Ollama - Local LLM)

🚀 Offline AI chatbot powered by Ollama with voice interaction, emotion detection, and memory system.

---

## ✨ Features
- 📴 Works completely offline (no API required)
- 🧠 Persistent memory using JSON
- 😊 Emotion detection system
- 🎤 Voice input (Speech-to-Text)
- 🔊 Voice output (Text-to-Speech)
- ⚡ Fast response using local LLM (Ollama)
- 🧩 Modular Python architecture

---

## 🛠️ Tech Stack
- Python
- Ollama (Local LLM)
- SpeechRecognition / TTS
- JSON (for memory storage)

---

## 📂 Project Structure
main.py # Main chatbot logic
memory.py # Memory system
emotion.py # Emotion detection
memory.json # Stored data
tts_test.py # Text-to-speech test
voice_test.py # Voice input test

---

## ⚙️ Setup Instructions

### 1. Install Ollama
Download from: https://ollama.com

### 2. Run LLM model
```bash
ollama run llama3

pip install -r requirements.txt

python main.py
