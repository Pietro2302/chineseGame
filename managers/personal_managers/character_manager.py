import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from inventory_class import EquipmentSlot,Item,InventoryManager
from quest_class import QuestsManager
from relationship_class import RelationshipsManager
from reputation_class import ReputationsManager
from skills_class import SkillsManager
from title_class import TitlesManager
from common_functions import save_character
from rich.console import Console


class CharacterManager:
    def __init__(self, character):
        self.inventoryManager = InventoryManager()
        self.questManager = QuestsManager()
        self.relationshipManager = RelationshipsManager()
        self.reputationManager = ReputationsManager()
        self.skillManager = SkillsManager()
        self.titleManager = TitlesManager()
        inventory = InventoryManager()
