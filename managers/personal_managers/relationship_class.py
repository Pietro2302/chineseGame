from enum import Enum


class RelationshipType(Enum):
    FRIENDSHIP = "Friendship"
    RIVALRY = "Rivalry"
    HOSTILITY = "Hostility"
    ADMIRATION = "Admiration"
    FEAR = "Fear"

    def __str__(self):
        return self.value


class Relationship:
    def __init__(
        self,
        nameFirstPerson: str,
        nameSecondPerson: str,
        relationship_type: RelationshipType,
        value: int = 0,
    ):
        self.firstPerson = nameFirstPerson
        self.secondPerson = nameSecondPerson
        self.relationship_type = relationship_type
        self.value = value

    def __str__(self):
        return (
            f"{self.firstPerson} {self.relationship_type} "
            f"({self.value}) {self.secondPerson}"
        )


class RelationshipsManager:
    def __init__(self):
        self.npc_relations = {}
        self.factions_relations = {}

    def to_dict(self):
        return {
            "npc_relations": self.npc_relations,
            "factions_relations": self.factions_relations
        }
