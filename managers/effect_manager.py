from typing import Callable,Dict,Any
from .effects_registry import register_effect, effects_registry


class Effect: 
    def __init__(self, effect_type: str, params: Dict[str,Any]):
        self.effect_type = effect_type
        self.params = params

    def __str__(self):
        return f"Effect(type={self.effect_type}, params={self.params})"

class EffectManager:
    def __init__(self):
        self.effects_registry: Dict[str, Callable[[Effect,Any], None]] = effects_registry
    
    def execute_effect(self, effect: Effect, target: Any):
        effect_func = self.effects_registry.get(effect.effect_type)
        if effect_func:
            effect_func(effect,target)
        else:
            print(f"[EffectHandler] No effect registered for type {effect.effect_type}.")

@register_effect("currency")
def apply_currency_effect(effect: Effect, target: Any) -> None:
    amount = effect.params.get("amount", 0)
    target.currency += amount
    print(f"[Effect] Applied currency effect: {amount} to {target.first_name}")

@register_effect("xp")
def apply_xp_effect(effect:Effect, target: Any) -> None:
    amount = effect.params.get("amount", 0)
    target.xp += amount
    print(f"[Effect] Applied xp effect: {amount} to {target.first_name}")

@register_effect("buff")
def apply_buff_effect(effect: Effect, target: Any) -> None:
    buff = effect.params.get("buff", None)    
    if buff == None:
        print(f"[Effect] No buff detected")
        return
    if "Temporary" not in target.buffs:
        target.buffs["Temporary"] = {}
    if "Permanent" not in target.buffs:
        target.buffs["Permanent"] = {}

    if buff["type"] == "temporary":
        target.buffs["Temporary"][buff["name"]] = buff
        print(f"[Effect] Applied Temporary Buff: {buff["name"]} to {target.first_name}")
    elif buff["type"] == "permanent":
        target.buffs["Permanent"][buff["name"]] = buff
        print(f"[Effect] Applied Permanent Buff: {buff["name"]} to {target.first_name}")
    

