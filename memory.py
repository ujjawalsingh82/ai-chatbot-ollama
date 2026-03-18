import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(BASE_DIR, "memory.json")

# load or create memory
if os.path.exists(FILE):
    with open(FILE, "r") as f:
        memory = json.load(f)
else:
    memory = {
        "name": None,
        "last_emotion": None,
        "last_message": None
    }
    with open(FILE, "w") as f:
        json.dump(memory, f)

def save():
    with open(FILE, "w") as f:
        json.dump(memory, f)

def update_memory(name=None, emotion=None, message=None):
    if name:
        memory["name"] = name
    if emotion:
        memory["last_emotion"] = emotion
    if message:
        memory["last_message"] = message
    save()

def get_memory():
    return memory
