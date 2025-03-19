import uuid
from managers.personal_managers.character_manager import CharacterManager


class Character:
    def __init__(self, 
                first_name, family_name, gender,
                level=0, xp=0, attributes=None,
                skills=None, relationships=None,
                inventory=None, quests=None, reputation=None,
                    titles=None):
        self.id = str(uuid.uuid4())
        self.first_name = first_name
        self.family_name = family_name
        self.gender = gender
        self.level = level
        self.xp = xp
        self.attributes = attributes if attributes is not None else {
            "strength": 10, "dexterity": 10, "constitution": 10,
            "intelligence": 10, "wisdom": 10, "charisma": 10
        }
        self.skills = skills if skills is not None else {}
        self.relationships = relationships if relationships is not None else {}
        self.inventory = inventory if inventory is not None else {}
        self.quests = quests if quests is not None else {}
        self.reputation = reputation if reputation is not None else {}
        self.titles = titles if titles is not None else {}
        self.characterManager = CharacterManager(self)

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'family_name': self.family_name,
            'gender': self.gender,
            'level': self.level,
            'xp': self.xp,
            'attributes': self.attributes,
            'skills': self.skills,
            'relationships': self.relationships,
            'inventory': self.inventory,
            'quests': self.quests,
            'reputation': self.reputation,
            'titles': self.titles
        }

    def __str__(self):
        return str(self.to_dict())
