class Buff:
    def __init__(self, buff_type: str, effects: dict):
        if buff_type not in ["Temporary", "Permanent"]:
            raise ValueError("buff_type must be either 'Temporary' or 'Permanent'")
        self.buff_type = buff_type
        self.effects = effects


class BuffsManager:
    def __init__(self,permanent_buffs = None, temporary_buffs = None):
        self.permanent_buffs = permanent_buffs if permanent_buffs is not None else {}
        self.temporary_buffs = temporary_buffs if temporary_buffs is not None else {}
        print("BUFFS MANAGER:")
        print(self)

    def add_buff(self, buff_name: str, buff: Buff):
        if buff.buff_type == "Temporary":
            self.temporary_buffs[buff_name] = buff
        elif buff.buff_type == "Permanent":
            self.permanent_buffs[buff_name] = buff
    
    def remove_buff(self, buff_name: str):
        if buff_name in self.temporary_buffs:
            del self.temporary_buffs[buff_name]
        elif buff_name in self.permanent_buffs:
            del self.permanent_buffs[buff_name]
    
    def get_buff(self, buff_name: str):
        return self.temporary_buffs.get(buff_name) or self.permanent_buffs.get(buff_name)
    
    def to_dict(self):
        return {
            "Temporary": {name: buff.to_dict() for name, buff in self.temporary_buffs.items()},
            "Permanent": {name: buff.to_dict() for name, buff in self.permanent_buffs.items()},
        }
    
    def __str__(self):
        return(str(self.to_dict()))

