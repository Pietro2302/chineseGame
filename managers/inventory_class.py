from enum import Enum
from styles import narrator_print
class EquipmentSlot(Enum):
    BOTTOM = "bottom"
    TOP = "top"
    LEFTHAND = "lefthand"
    RIGHTHAND = "righthand"
    HEAD = "head"
    BAG = "bag"


class Item:
    def __init__(self, name, item_type: EquipmentSlot, description, effects):
        self.name = name
        self.item_type = item_type
        self.description = description
        self.effects = effects

    def __str__(self):
        return f"{self.name} ({self.item_type}): {self.description}"


class InventoryManager:
    def __init__(self, bottom = None, top = None, leftHand = None, rightHand = None, head = None, bag = None):
        self.items = {}
        self.bottom = bottom if bottom is not None else {}
        self.top = top if top is not None else {}
        self.leftHand = leftHand if leftHand is not None else {}
        self.rightHand = rightHand if rightHand is not None else {}
        self.head = head if head is not None else {}
        self.bag = bag if bag is not None else {}


    def assignItem(self, recepient: EquipmentSlot, item, console):
        if not (isinstance(item, Item) and recepient == item.item_type):
            print("Item assignment failed.")
            return
        self.items[item.name] = item
        match item.item_type:
            case EquipmentSlot.BOTTOM:
                if len(self.bottom) <= 1:
                    self.bottom[item.name] = item
                else:
                    narrator_print("It seems like you have already something equipped there. I shall put it in the bag!")
                    if len(self.bag) <= 10:
                        self.bag[item.name] = item
                        return
                    else:
                        narrator_print("It seems like the bag is already fill. Let's try another time !")
            case EquipmentSlot.TOP:
                if len(self.top) <= 1:
                    self.top[item.name] = item
                else:
                    return
            case EquipmentSlot.RIGHTHAND:              
                if len(self.rightHand) <= 1:
                    self.rightHand[item.name] = item
                else:
                    return
            case EquipmentSlot.LEFTHAND:
                if len(self.leftHand) <= 1:
                    self.leftHand[item.name] = item
                else:
                    return
            case EquipmentSlot.HEAD:
                if len(self.head) <= 1:
                    self.head[item.name] = item
                else:
                    return
            case EquipmentSlot.BAG:
                if len(self.bag) <= 10:
                    self.bag[item.name] = item
                else:
                    return
                          

