from typing import Dict, Callable
effects_registry: Dict[str, Callable] = {}
def register_effect(effect_type: str):
    def decorator(func: Callable):
        effects_registry[effect_type] = func
        return func
    return decorator