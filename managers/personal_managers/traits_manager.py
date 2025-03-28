from effect_manager import Effect
from typing import Dict,Any
class Trait: 
    def __init__(self, name : str, effects: Dict[Effect,Any], requirements: dict, point_value: int):
        if name is None: 
            raise ValueError("Name of the trait is None, please insert a valid name")
        elif not isinstance(name, str):
            raise TypeError("Name must be a string, please insert a string")
        if effects is None:
            raise ValueError("Effects of the trait is None, please insert a valid dictionary of effects")
        elif not isinstance(effects, dict):
            raise TypeError("Effects is not a dictionary, please insert a valid dictionary of effects")
        for effect in effects:
            if not isinstance(effect,Effect):
                raise TypeError("All of the Effects in the effects dictionary must be Effects of the Effect type.")
        
        if not isinstance(requirements,dict):
            raise TypeError("Requirements is not a dictionary, please insert a valid dictionary of requirements")
        if point_value is None:
            raise ValueError("Point Values of the trait is None, please insert a valid point value")
        elif not isinstance(point_value,int):
            raise TypeError("Point Value of the trait needs to be an int, please insert a valid int for the point value")
        
        self.name = name
        self.effects = effects
        self.requirements = requirements if requirements is not None else {}
        self.point_value = point_value

    
    def getTraitName(self):
        return self.name
    def getTraitEffects(self):
        return self.effects
    def getTraitRequirements(self):
        return self.requirements
    def getTraitPointValue(self):
        return self.point_value
    def setTraitName(self, newName: str):
        if newName is None:
            raise ValueError("Name of the trait is None, please insert a valid name")
        elif not isinstance(newName, str):
            raise TypeError("Name must be a string, please insert a string")
        self.name = newName
    def setTraitEffects(self, effects:Dict[Effect,Any]):
        if effects is None:
            raise ValueError("Effects of the trait is None, please insert a valid dictionary of effects")
        elif not isinstance(effects, dict):
            raise TypeError("Effects is not a dictionary, please insert a valid dictionary of effects")
        for effect in effects:
            if not isinstance(effect,Effect):
                raise TypeError("All of the Effects in the effects dictionary must be Effects of the Effect type.")
        
        self.effects = effects
    
    def setTraitRequirements(self, requirements: dict):
        if not isinstance(requirements,dict):
            raise TypeError("Requirements is not a dictionary, please insert a valid dictionary of requirements")
        self.requirements = requirements
    
    def setTraitPointValue(self, point_value:int):
        if point_value is None:
            raise ValueError("Point Values of the trait is None, please insert a valid point value")
        elif not isinstance(point_value,int):
            raise TypeError("Point Value of the trait needs to be an int, please insert a valid int for the point value")
        self.point_value = point_value
    
    def addEffect(self, newEffect: Effect):
        if newEffect is None:
            raise ValueError("newEffect is None, please insert a valid Effect")
        elif not isinstance(newEffect,Effect):
            raise TypeError("newEffect is not an Effect Type, please insert a valid Effect Type")
        effects_dict = self.effects.copy()
        dict_length = len(self.effects)
        self.effects[newEffect.name] = newEffect
        if dict_length != len(self.effects)+1:
            self.effects = effects_dict
            raise RuntimeError("The addition of the new Effect went wrong, ripristinating everything")
        if newEffect not in self.effects:
            self.effects = effects_dict
            raise RuntimeError("The addition of the new Effect went wrong , ripristinating everything")

        for effect in effects_dict:
            if effect not in self.effects:
                self.effects = effects_dict
                raise RuntimeError("The addition of the new Effect went wrong, it ovverode an old effect")
    
    def addRequirement(self, newRequirement):
        if newRequirement is None: 
            raise ValueError("newRequirement is None, please insert a valid Requirement")
        oldRequirements = self.requirements.copy()
        dict_lenght = len(self.requirements)
        self.requirements[newRequirement.name] = newRequirement
        if dict_lenght != len(self.requirements)+1:
            self.requirements = oldRequirements
            raise RuntimeError("The addition of the new Requirement went wrong, ripristinating everything")
        if newRequirement not in self.requirements:
            self.requirements = oldRequirements
            raise RuntimeError("The addition of the new Requirement went wrong, ripristinating everything")
        
        for requirement in oldRequirements:
            if requirement not in self.requirements:
                self.requirements = oldRequirements
                raise RuntimeError("The addition of the new Requirement went wrong, it ovverode an old requirement")
            
    
    def removeEffect(self, effect_name:str):
        if effect_name is None:
            raise ValueError("The effect name is None, insert a valid name")
        elif not isinstance(effect_name,str):
            raise TypeError("The effect name is not a string, please insert a valid string")
        elif effect_name not in self.effects:
            raise ValueError("The effect is not in the effects, please insert an effect in the effects dict")
        
        del(self.effects[effect_name])
    
    def removeRequirement(self, requirement_name:str):
        if requirement_name is None:
            raise ValueError("The requirement name is None, insert a valide name")
        elif not isinstance(requirement_name,str):
            raise TypeError("The requirement name is not a string, please insert a valid string")
        elif requirement_name not in self.requirements:
            raise ValueError("The requirement is not in the requirements, please insert a requirement in the requirements dict")
        
        del(self.requirements[requirement_name])


class TraitsManager:
    def __init__(self, traits: Dict[Trait,Any]):
        if not isinstance(traits,dict) and traits is not None:
            raise TypeError("The traits needs to be a dict, please insert a dictionary")
        for trait in traits: 
            if not isinstance(trait,Trait):
                raise TypeError("The traits dict needs to be a dictionary of trait. One of the traits is not a Trait type")
        
        self.traits = traits if traits is not None else {}


    def getTraits(self):
        return self.traits
    def setTraits(self, traits: Dict[Trait,Any]):
        if traits is None:
            raise ValueError("The traits is None, please insert a valid dictionary")
        elif not isinstance(traits,dict):
            raise TypeError("The traits needs to be a dict, please insert a dictionary")
        for trait in traits: 
            if not isinstance(trait,Trait):
                raise TypeError("The traits dict needs to be a dictionary of trait. One of the traits is not a Trait type")
        
        self.traits = traits
    
    def addTrait(self, trait:Trait):
        if trait is None: 
            raise ValueError("The trait is None, please insert a valid Trait")
        elif not isinstance(trait, Trait):
            raise TypeError("The trait needs to be a Trait type, please insert a valid trait")
        oldTraits = self.traits.copy()
        traits_len = len(self.traits)
        self.traits[trait.name] = trait
        if traits_len != len(self.traits)+1:
            self.traits = oldTraits
            raise RuntimeError("The trait addition didn't work, so restoring everything back to normality")
        if trait not in self.traits:
            self.traits = oldTraits
            raise RuntimeError("The trait addtion didn't work, so restoring everything back to normality")
        
        for trait in oldTraits: 
            if trait not in self.traits:
                self.traits = oldTraits
                raise RuntimeError("The trait addition didn't work, so restoring everything back to normality, one of the old effects was ovveridden")

    def removeTrait(self, trait_name:str):
        if trait_name is None: 
            raise ValueError("The name is None , please insert a valid name")
        elif not isinstance(trait_name, str):
            raise TypeError("The name is not a string , please insert a valid string")
        elif trait_name not in self.traits:
            raise ValueError("The trait name is not in the traits, please insert a valid trait")
        del(self.traits[trait_name])        
        

