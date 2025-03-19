from styles import narrator_print
from rich import box
from rich.table import Table
from character_class import Character
from common_functions import load_characters, save_character
import time
import questionary
import os
import copy

characters_filename = "character_player.json"


def new_Game(console):
    os.system('cls')
    narrator_print(
        "Firstly, you must choose your character's first name. "
        "What is your name, Roman?",
        console,
    )
    first_name = input("> ")
    os.system('cls')
    narrator_print("What is your gender?", console)
    gender = input("> ")
    os.system('cls')
    narrator_print(
        f"Ah, {first_name}! Such a wonderful name, indeed. In ancient Rome, "
        "family names held great significance. They represented not just "
        "lineage, but honor, legacy, and the deeds of those who bore them. "
        "A Roman name carried the weight of one’s ancestors, shaping one's "
        "identity and place in society. Allow me, then, to speak of these "
        "legendary families, whose names echo through the annals of our "
        "history, their deeds immortalized in the very fabric of Rome itself.",
        console,
    )
    input("Press Enter to continue...")
    os.system('cls')
    narrator_print(
        "First, let us speak of the Scipii, the Masters of Warfare. Born of "
        "noble blood and forged in battle, the Scipii are a family destined "
        "for greatness. Under Publius Cornelius Scipio Africanus, they "
        "shattered Hannibal and secured Rome’s supremacy. Known for "
        "brilliant strategy and unstoppable armies, their legacy is written "
        "in the blood of their foes and built on the ruins of those who dared "
        "oppose Rome.",
        console,
    )
    input("Press Enter to continue...")
    os.system('cls')
    narrator_print(
        "Next, we have the Julians, the Political Titans. Descendants of "
        "Aeneas and blessed with a divine lineage, the Julians mastered "
        "diplomacy and imperial ambition. Julius Caesar, conqueror and "
        "revolutionary, sought not just power in the Senate, but dominion "
        "over the world. Under Augustus, they ushered in the era of empire, "
        "with a peace forged by their iron will. Their grip on Rome is "
        "absolute, shaping the empire from behind the shadows.",
        console,
    )
    input("Press Enter to continue...")
    os.system('cls')
    narrator_print(
        "Then there are the Claudii, the Imperial Dynasty. Born to rule with "
        "fierce authority, the Claudii are defined by their unyielding "
        "control. With Tiberius, the empire was held in cold, calculated "
        "power. Caligula, unpredictable and tyrannical, sought to reshape "
        "the world at his whim. Yet, even in turmoil, the Claudii expanded "
        "and transformed Rome, bending the empire to their will.",
        console,
    )
    input("Press Enter to continue...")
    os.system('cls')
    narrator_print(
        "Finally, the Flavians, the Builders of Legacy. Rising from civil war,"
        "the Flavians restored the empire under Vespasian, bringing peace "
        "and stability. Titus, his son, faced the eruption of Vesuvius and "
        "constructed the mighty Colosseum, a symbol of Rome’s enduring "
        "strength. The Flavians are builders, not conquerors—shaping Rome’s "
        "future with monumental projects and lasting foundations.",
        console,
    )
    input("Press Enter to continue...")
    os.system('cls')
    narrator_print(
        "So, fili mii, to what family do you belong to? Be careful, since "
        "this will shape your future and your destiny. Dī bene vertant!",
        console,
    )
    family_choice = questionary.select(
        "",
        choices=[
            "The Scipius family",
            "The Julian family",
            "The Claudius family",
            "The Flavius family",
            "I belong to no family. (Warning: highest difficulty)"
        ]
    ).ask()

    if "no family" in family_choice:
        family_choice = "no_family"

    os.system('cls')
    match family_choice:
        case "The Scipius family":
            family_name = "Scipio"
            message = (
                f"Welcome to Rome, {first_name} {family_name}, "
                "may you become a fine warrior and a mighty general!"
            )
        case "The Julian family":
            family_name = "Julius"
            message = (
                f"Welcome to Rome, Julius {first_name}, "
                "may you climb the political ladder in a heartbeat!"
            )
        case "The Claudius family":
            family_name = "Claudius"
            message = (
                f"Welcome to Rome, {first_name} {family_name}, "
                "may your power over the Imperium be unyielding!"
            )
        case "The Flavius family":
            family_name = "Flavius"
            message = (
                f"Welcome to Rome, Flavius {first_name}, "
                "may your buildings reach for the sky!"
            )
        case "no_family":
            narrator_print(
                "Welcome to Rome, bold one. Please, choose a family name "
                "for yourself, one that will echo through the Imperium "
                "forever!",
                console,
            )
            family_name = input("> ")
    narrator_print(message, console)

    player_character = Character(first_name, family_name, gender)
    save_character(player_character.to_dict())


def displaySaveGames(console):
    characters_dict = load_characters(characters_filename)
    if not characters_dict:
        narrator_print(
            "It seems like you haven't "
            "yet saved any Romans."
            "Go back to the menu "
            "and start a new game!",
            console,)
        return
    character_choices = [
        (
            char["id"],
            f"{char['first_name']} {char['family_name']}"
        )
        for char in characters_dict
        if "first_name" in char and "family_name" in char
    ]
    loading_choice = questionary.select(
        " ", choices=[name for _, name in character_choices]
    ).ask()
    os.system('cls')        
    selected_id = next(
        id for id, name in character_choices if name == loading_choice
    )
    char_choice = next(
        char for char in characters_dict if char["id"] == selected_id
    )
    char_table = Table(box=box.DOUBLE_EDGE)
    char_table.add_column(
        f"{char_choice['first_name']} {char_choice['family_name']} "
        f"Level: {char_choice['level']}"
    )
    console.print(char_table)
    narrator_print("Do you wish to load this character ?", console)
    toload = questionary.select(
        "", choices=["Yes", "No"]).ask()
    if (toload == "Yes"):
        load_Game(char_choice)
    else:
        os.system('cls')
        narrator_print(
            "Choose one of the characters you have previously saved:",
            console,
        )
        displaySaveGames(console)


def load_Game(character):
    player_char = Character(
        character['first_name'],
        character['family_name'],
        character['gender'],
        character['level'],
        character['xp'],
        character['attributes'],
        character['skills'],
        character['relationships'],
        character['inventory'],
        character['quests'],
        character['reputation'],
        character['titles'])
    time.sleep(1)
