import sys
import os
import uuid
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from inventory_class import InventoryManager
from quest_class import QuestsManager
from relationship_class import RelationshipsManager
from reputation_class import ReputationsManager
from skills_class import CharacterSkillsManager
from title_class import TitlesManager
from ..effect_manager import EffectManager
from buffs_manager import BuffsManager

class Character:
    def __init__(self, 
                first_name, family_name, gender, effectManager, 
                level=0, xp=0, currency=0, attributes=None,
                skills=None, relationships=None,
                inventory=None, quests=None, reputation=None,
                    titles=None, buffs=None):
        self.id = str(uuid.uuid4())
        self.first_name = first_name
        self.family_name = family_name
        self.gender = gender
        self.level = level
        self.xp = xp
        self.currency = currency 
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
        self.buffs = buffs if buffs is not None else {}
        self.characterManager = CharacterManager(self, effectManager)

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'family_name': self.family_name,
            'gender': self.gender,
            'level': self.level,
            'xp': self.xp,
            'currency': self.currency,
            'attributes': self.attributes,
            'skills': self.skills,
            'relationships': self.relationships,
            'inventory': self.inventory,
            'quests': self.quests,
            'reputation': self.reputation,
            'titles': self.titles,
            'buffs': self.buffs
        }

    def __str__(self):
        return str(self.to_dict())


class CharacterManager:
    def __init__(self, character: Character, effectManager : EffectManager):
        self.inventoryManager = InventoryManager(character.inventory.get("bottom"),character.inventory.get("top"),character.inventory.get("leftHand"),character.inventory.get("rightHand"),character.inventory.get("head"),character.inventory.get("bag"))
        self.questManager = QuestsManager(character.quests.get("active_quests"),character.quests.get("completed_quests"))
        self.relationshipManager = RelationshipsManager(character.relationships.get("npc_relations"),character.relationships.get("factions_relations"))
        self.reputationManager = ReputationsManager(character.reputation.get("reputations"))
        self.skillManager = CharacterSkillsManager(character.skills)
        self.titleManager = TitlesManager(character.titles)
        self.buffsManager = BuffsManager(character.buffs.get("Permanent"),character.buffs.get("Temporary"))
        self.effectManager = effectManager
        print(character)
        
