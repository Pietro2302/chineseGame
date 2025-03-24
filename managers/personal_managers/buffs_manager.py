class Buff:
    def __init__(self, name:str, buff_type: str, effects: dict):
        if buff_type not in ["Temporary", "Permanent"]:
            raise ValueError("buff_type must be either 'Temporary' or 'Permanent'")
        self.name = name
        self.buff_type = buff_type
        self.effects = effects


class BuffsManager:
    def __init__(self,permanent_buffs = None, temporary_buffs = None):
        if permanent_buffs is not None and not isinstance(permanent_buffs, dict):
            raise TypeError("permanent_buffs must be a dictionary of Buff objects.")
        if temporary_buffs is not None and not isinstance(temporary_buffs, dict):
            raise TypeError("temporary_buffs must be a dictionary of Buff objects.")

        if permanent_buffs:
            for key, value in permanent_buffs.items():
                if not isinstance(value, Buff):
                    raise TypeError(f"Permanent buff '{key}' is not a Buff object.")
        
        if temporary_buffs:
            for key, value in temporary_buffs.items():
                if not isinstance(value, Buff):
                    raise TypeError(f"Temporary buff '{key}' is not a Buff object.")
                
        self.permanent_buffs = permanent_buffs or {}
        self.temporary_buffs = temporary_buffs or {}

    def add_buff(self, buff: Buff):
        if not isinstance(buff,Buff) or buff is None:
            raise TypeError(f"The buff provided '{buff}' is not a Buff object.")
        if buff.buff_type == "Temporary":
            self.temporary_buffs[buff.name] = buff
        elif buff.buff_type == "Permanent":
            self.permanent_buffs[buff.name] = buff
    
    def remove_buff(self, buff_name: str):
        if buff_name in self.temporary_buffs:
            del self.temporary_buffs[buff_name]
        elif buff_name in self.permanent_buffs:
            del self.permanent_buffs[buff_name]
        else:
            raise KeyError(f"Buff '{buff_name}' not found in the BuffsManager.")

    def get_buff(self, buff_name: str):
        buff = self.temporary_buffs.get(buff_name) or self.permanent_buffs.get(buff_name)
        if buff is None:
            raise KeyError(f"Buff '{buff_name}' not found in the BuffsManager.")
        return buff
    
    def to_dict(self):
        return {
            "Temporary": self.temporary_buffs,
            "Permanent": self.permanent_buffs,
        }
    
    def __str__(self):
        return(str(self.to_dict()))

