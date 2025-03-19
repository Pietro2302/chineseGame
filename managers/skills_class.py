import json


class Skill:
    def __init__(self, name, skill_type, effects, is_active,
                 combat_only, cooldown, stamina_cost,
                 requirements):
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


class SkillsManager:
    def __init__(self, skills_file="managers/skills.json"):
        self.skills = {}
        self.load_skills(skills_file)
        self.cooldowns = {}

    def load_skills(self, filename):
        with open(filename, "r") as file:
            skills_data = json.load(file)
            for skill_data in skills_data:
                skill = Skill(**skill_data)
                self.skills[skill.name] = skill
