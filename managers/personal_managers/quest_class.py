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
    def __init__(self, active_quests = None, completed_quests = None):
        self.active_quests = active_quests if active_quests is not None else {}
        self.completed_quests = completed_quests if completed_quests is not None else {}
        print("QUESTS MANAGER:")
        print(self)

    def to_dict(self):
        return {
            "active_quests": self.active_quests,
            "completed_quests": self.completed_quests
        }
    def __str__(self):
        return str(self.to_dict())
