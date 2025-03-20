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
    def __init__(self, titles = None):
        self.titles = titles if titles is not None else {}
        print("TITLE MANAGER:")
        print(self)

    def to_dict(self):
        return {title_name: {
                "effects": title.effects,
                "description": title.description
            }for title_name, title in self.titles.items()}

    def __str__(self):
        return str(self.to_dict())
