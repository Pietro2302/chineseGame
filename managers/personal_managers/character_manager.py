import sys
import os
import uuid
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from managers.personal_managers.inventory_class import InventoryManager, Item
from managers.personal_managers.quest_class import QuestsManager, Quest
from managers.personal_managers.relationship_class import RelationshipsManager, Relationship
from managers.personal_managers.reputation_class import ReputationsManager
from managers.personal_managers.skills_class import Skill, CharacterSkillsManager
from managers.personal_managers.title_class import TitlesManager, Title
from managers.effect_manager import EffectManager
from managers.personal_managers.buffs_manager import BuffsManager, Buff

class Character:
    def __init__(self, 
                first_name:str, family_name:str, gender:str, effectManager:EffectManager, 
                level=0, xp=0, currency=0, attributes=None,
                skills=None, relationships=None,
                inventory=None, quests=None, reputation=None,
                    titles=None, buffs=None):
        self.id = str(uuid.uuid4())
        valid_genders = {"Male", "Female", "Other"}
        default_attributes = {
            "strength": 10, "dexterity": 10, "constitution": 10,
            "intelligence": 10, "wisdom": 10, "charisma": 10
        }
        default_relationships = {
            "npc_relations": {},
            "factions_relations": {}
        }
        default_inventory = {
            "items": {},
            "bottom": {},
            "top": {},
            "leftHand": {},
            "rightHand": {},
            "head": {},
            "bag": {}
        }
        default_quests = {
            "active_quests": {},
            "completed_quests": {}
        }
        default_reputations = { 
            "Honorable": 0,
            "Feared": 0,
            "Corrupt": 0,
            "Neutral": 0,
            "Noble": 0,
            "Infamous": 0,
            "Treacherous": 0,
            "Dignified": 0,
            "Deceitful": 0,
            "Brave": 0,
            "Cunning": 0,
            "Tyrannical": 0
        }
        default_titles = {}
        default_buffs = {
            "Temporary": {},
            "Permanent": {}
        }
        if gender is not None:
            if gender not in valid_genders:
                raise ValueError(f"Invalid gender '{gender}'. Allowed values: {valid_genders}")
        if level is not None:
            if not isinstance(level, int) or level < 0:
                raise TypeError(f"Invalid level '{level}', the level value should be a positive integer")
        if xp is not None:
            if not isinstance(xp, int) or xp < 0:
                raise TypeError(f"Invalid xp '{xp}', the xp should be a positive integer")
        if currency is not None:
            if not isinstance(currency, float):
                raise TypeError(f"Invalid currency '{currency}', the currency should be a float")

        if attributes is not None:
            if not isinstance(attributes,dict):
                raise TypeError("Attributes must be a dictionary")
            expected_keys = set(default_attributes.keys())
            if set(attributes.keys()) != expected_keys:
                raise ValueError(f"Attributes must contain exactly these keys: {expected_keys}")
            for key, value in attributes.items():
                if not isinstance(value,int) or value < 0 :
                    raise TypeError(f"Attribute '{key}' must be a positive integer.")
        
        if skills is not None:
            if not isinstance(skills,dict):
                raise TypeError("Skills must be a dictionary")
            for key, value in skills.items():
                if not isinstance(value,Skill):
                    raise TypeError(f"Skill '{key}' must be a skill.")
                
        if relationships is not None:
            if not isinstance(relationships,dict):
                raise TypeError("Relationship must be a dictionary")
            expected_keys = set(default_relationships.keys())
            if set(relationships.keys()) != expected_keys:
                raise ValueError(f"Relationship must contain exactly these keys: {expected_keys}")
            for key, value in relationships.items():
                if not isinstance(value,Relationship):
                    raise TypeError(f"Relationship '{key}' must be a relationship.")
        
        if inventory is not None:
            if not isinstance(inventory, dict):
                raise TypeError("Inventory must be a dictionary")
            expected_keys = set(default_inventory.keys())
            if set(inventory.keys()) != expected_keys:
                raise ValueError(f"Inventory must contain exactly these keys: {expected_keys}")
            for key, value in inventory.items():
                if not isinstance(value, Item):
                    raise TypeError(f"Inventory '{key}' must be an Item.")
        
        if quests is not None:
            if not isinstance(quests, dict):
                raise TypeError("Quests must be a dictionary")
            expected_keys = set(default_quests.keys())
            if set(quests.keys()) != expected_keys:
                raise ValueError(f"Quests must contain exactly these keys: {expected_keys}")
            for key, value in quests.items():
                if not isinstance(value, Quest):
                    raise TypeError(f"Quest '{key}' must be a Quest.")
        
        if reputation is not None:
            if not isinstance(reputation, dict):
                raise TypeError("Reputation must be a dictionary")
            expected_keys = set(default_reputations.keys())
        if set(reputation.keys()) != expected_keys:
            raise ValueError(f"Reputation must contain exactly these keys: {expected_keys}")
    
        if titles is not None:
            if not isinstance(titles, dict):
                raise TypeError("Titles must be a dictionary")
            for key, value in titles.items():
                if not isinstance(value, Title):
                    raise TypeError(f"Title '{key}' must be a Title.")

        if buffs is not None:
            if not isinstance(buffs, dict):
                raise TypeError("Buffs must be a dictionary")
            expected_keys = set(default_buffs.keys())
            if set(buffs.keys()) != expected_keys:
                raise ValueError(f"Buffs must contain exactly these keys: {expected_keys}")
            for key, value in buffs.items():
                if not isinstance(value, Buff):
                    raise TypeError(f"Buff '{key}' must be a Buff.")
        
        
        self.first_name = first_name
        self.family_name = family_name
        self.gender = gender
        self.level = level
        self.xp = xp
        self.currency = currency 
        self.attributes = attributes if attributes is not None else default_attributes
        self.skills = skills if skills is not None else {}
        self.relationships = relationships if relationships is not None else default_relationships
        self.inventory = inventory if inventory is not None else default_inventory
        self.quests = quests if quests is not None else default_quests
        self.reputation = reputation if reputation is not None else default_reputations
        self.titles = titles if titles is not None else default_titles
        self.buffs = buffs if buffs is not None else default_buffs
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
        if character is None:
            raise ValueError("The character object is None, please insert a valid object.")
        elif not isinstance(character,Character):
            raise TypeError("character must be a Character Object")
        if effectManager is None:
            raise ValueError("The effectManager object is None, please insert a valid object.")
        elif not isinstance(effectManager,EffectManager):
            raise TypeError("effectManager must be a EffectManager Object")
        self.inventoryManager = InventoryManager(character.inventory.get("bottom"),character.inventory.get("top"),character.inventory.get("leftHand"),character.inventory.get("rightHand"),character.inventory.get("head"),character.inventory.get("bag"))
        self.questManager = QuestsManager(character.quests.get("active_quests"),character.quests.get("completed_quests"))
        self.relationshipManager = RelationshipsManager(character.relationships.get("npc_relations"),character.relationships.get("factions_relations"))
        self.reputationManager = ReputationsManager(character.reputation.get("reputations"))
        self.skillManager = CharacterSkillsManager(character.skills)
        self.titleManager = TitlesManager(character.titles)
        self.buffsManager = BuffsManager(character.buffs.get("Permanent"),character.buffs.get("Temporary"))
        self.effectManager = effectManager
        
        
