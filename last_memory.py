# last_memory.py

def get_last_summary(memory):
    summary = []

    if memory.get("name"):
        summary.append(f"User name is {memory['name']}")

    if memory.get("last_emotion"):
        summary.append(f"Last emotion was {memory['last_emotion']}")

    if memory.get("last_message"):
        summary.append(f"Last message was: {memory['last_message']}")

    return " | ".join(summary)
