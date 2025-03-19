class Quest:
    def __init__(self, name, description, objectives, reward):
        self.name = name
        self.description = description
        self.objectives = objectives
        self.reward = reward
        self.status = "active"

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "objectives": self.objectives,
            "reward": self.reward,
            "status": self.status
        }


class QuestsManager:
    def __init__(self):
        self.active_quests = []
        self.completed_quests = []

    def to_dict(self):
        return {
            "active_quests": self.active_quests,
            "completed_quests": self.completed_quests
        }
