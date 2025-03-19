import json
from enum import Enum
import os
FILENAME = "characters.json"

class MessageType(Enum):
    INFO = "INFO"             # General information
    WARNING = "WARNING"       # Non-critical issue
    ERROR = "ERROR"           # Critical issue or failure
    COMBAT = "COMBAT"         # Combat-related messages
    DIALOGUE = "DIALOGUE"     # NPC conversations
    QUEST = "QUEST"           # Quest-related updates
    SKILL = "SKILL"           # Skill usage or unlock notifications
    INVENTORY = "INVENTORY"   # Item usage, acquisition, or loss
    SYSTEM = "SYSTEM"


def load_characters():
    """Load characters from a JSON file as a dictionary, using character ID as the key."""
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as json_file:
            try:
                return json.load(json_file)  # Load as dictionary
            except json.JSONDecodeError:
                return {}  # If file is empty or corrupted, return an empty dictionary
    return {}  # If file does not exist, return an empty dictionary

def save_character(new_character):
    """Save or update a character in the JSON file, using character ID as the key."""
    characters = load_characters()  # Load existing characters

    character_id = new_character["id"]  # Use ID as the key
    characters[character_id] = new_character  # Update or add new character

    # Save the updated dictionary back to the file
    with open(FILENAME, "w") as json_file:
        json.dump(characters, json_file, indent=4)

class GameMessage:
    def __init__(self, message_type, content, sender=None, recipient=None):
        self.message_type = MessageType
        self.content = content
        self.sender = sender
        self.recipient = recipient

    def __repr__(self):
        sender = f"[{self.sender}]" if self.sender else "[SYSTEM]"
        return f"{sender} [{self.message_type}] -> {self.content}"


class GameResult:
    def __init__(self, success, message, data=None):
        self.success = success
        self.message = GameMessage
        self.data = data  # Può contenere informazioni extra utili

    def __repr__(self):
        return (
            f"GameResult(success={self.success},"
            f"message='{self.message},"
            f"data={self.data})"
        )
