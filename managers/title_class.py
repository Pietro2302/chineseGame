class Title:
    def __init__(self, name, effects=None, description=None):
        self.name = name
        self.effects = effects
        self.description = description

    def __str__(self):
        return self.name

    def get_effects(self):
        return self.effects

    def get_description(self):
        return self.description


class TitlesManager:
    def __init__(self):
        self.titles = {}

    def to_dict(self):
        return {title.name: effects for title, effects in self.titles.items()}
