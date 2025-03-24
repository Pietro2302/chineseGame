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
        firstID: int,
        secondID: int,
        relationship_type: RelationshipType,
        value: int = 0,
    ):
        self.firstID = firstID
        self.secondID = secondID
        self.relationship_type = relationship_type
        self.value = value

    def __str__(self):
        return (
            f"{self.firstID} {self.relationship_type} "
            f"({self.value}) {self.secondID}"
        )


class RelationshipsManager:
    def __init__(self, npc_relations = None, factions_relations = None):
        self.npc_relations = npc_relations if npc_relations is not None else {}
        self.factions_relations = factions_relations if factions_relations is not None else {}
    def to_dict(self):
        return {
            "npc_relations": self.npc_relations,
            "factions_relations": self.factions_relations
        }
    def __str__(self):
        return str(self.to_dict())
