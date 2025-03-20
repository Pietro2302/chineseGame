import managers
from managers.effect_manager import EffectManager, Effect
from managers.personal_managers.character_manager import Character
effect_manager = EffectManager()

effect = Effect("currency", {"amount": 100})
player = Character("Pietrus","Massarius","Male", effect_manager)
effect_manager.execute_effect(effect, player)
print(player)
effect2 = Effect("xp", {"amount": 10})
effect_manager.execute_effect(effect2,player)
print(player)
temporary_buff = {
    "name": "Strength Potion",
    "type": "temporary",
    "modifiers": {"strength": 5},  # Increases strength by 5
    "duration": 3  # Lasts for 3 turns
}

# Example of a permanent buff
permanent_buff = {
    "name": "Blessing of Wisdom",
    "type": "permanent",
    "modifiers": {"wisdom": 10}  # Increases wisdom by 10
}
effect4 = Effect(effect_type="buff", params={"buff": temporary_buff})
effect_manager.execute_effect(effect4,player)
print(player)