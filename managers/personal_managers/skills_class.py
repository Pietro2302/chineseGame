from enum import Enum

class SkillType(Enum):
    PERSONAL = "personal"
    MARTIAL = "martial"
    SOCIAL = "social"
    STRATEGIC = "strategic"
    SCHOLARLY = "scholarly"
    SURVIVAL = "survival"


class Skill:
    def __init__(self, name:str, skill_type:SkillType, effects:dict, is_active:bool,
                 combat_only:bool, cooldown:int, stamina_cost:int,
                 requirements:dict):
        self.name = name
        self.skill_type = skill_type
        self.is_active = is_active
        self.combat_only = combat_only
        self.cooldown = cooldown
        self.stamina_cost = stamina_cost
        self.requirements = requirements if requirements is not None else {}
        self.effects = effects

    def __repr__(self):
        return (
            f"Skill(name='{self.name}',"
            f" type='{self.skill_type}',"
            f" active={self.is_active})"
        )


class CharacterSkillsManager:
    def __init__(self, skills = None):
        self.skills = skills if skills is not None else {}

    def to_dict(self):
        return {
            "skills": self.skills,
        }

    def __str__(self):
        return str(self.to_dict())

