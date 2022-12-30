from ability import Ability, Weapon
import uuid

class Creature:
    
    def __init__(self, name, armor_class, hitpoints, speed, type, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.id = str(uuid.uuid1())[:4]
        self.name = name
        self.nick_name = name
        self.armor_class = armor_class
        self.hitpoints = hitpoints
        self.current_hitpoints = hitpoints
        self.speed = speed
        self.type = type
        self.strength_score = strength
        self.dexterity_score = dexterity
        self.constitution_score = constitution
        self.intelligence_score = intelligence
        self.wisdom_score = wisdom
        self.charisma_score = charisma
        self.current_hitpoints = self.hitpoints
        self.strength_bonus: int = self.calculate_bonus(self.strength_score)
        self.dexterity_bonus: int = self.calculate_bonus(self.dexterity_score)
        self.constitution_bonus: int = self.calculate_bonus(self.constitution_score)
        self.intelligence_bonus: int = self.calculate_bonus(self.intelligence_score)
        self.wisdom_bonus: int = self.calculate_bonus(self.wisdom_score)
        self.charisma_bonus: int = self.calculate_bonus(self.charisma_score)
        self.abilities = []
        self.weapons = []
        self.conditions = []
        
    
    def calculate_bonus(self, score):
        return (score - 10) // 2
    
    
    def add_ability(self, ability: Ability):
        self.abilities.append(ability)
        
    
    def add_weapon(self, weapon: Weapon):
        self.weapons.append(weapon)
        
    
    def rename(self, name: str):
        self.nick_name = name
        
    
    def set_id(self, id: int):
        self.id = id
        
    
    def __copy__(self):
        return Creature(self.name, 
                        self.armor_class, 
                        self.hitpoints, 
                        self.speed, 
                        self.type, 
                        self.strength_score, 
                        self.dexterity_score, 
                        self.constitution_score,
                        self.intelligence_score,
                        self.wisdom_score,
                        self.charisma_score)
        
    
    def __str__(self):
        name_string = 'Name: ' + self.name + ' (' + self.nick_name + ')'
        ac_string = 'AC: ' + str(self.armor_class)
        hp_string = 'HP: ' + str(self.hitpoints)
        currhp_string = 'Current HP: ' + str(self.current_hitpoints)
        speed_string = 'Speed: ' + str(self.speed)
        type_string = 'Type: ' + self.type
        
        strength_string = 'STR: ' + str(self.strength_score) + '(' + str(self.strength_bonus) + ')'
        dexterity_string = 'DEX: ' + str(self.dexterity_score) + '(' + str(self.dexterity_bonus) + ')'
        constitution_string = 'CON: ' + str(self.constitution_score) + '(' + str(self.constitution_bonus) + ')'
        intelligence_string = 'INT: ' + str(self.intelligence_score) + '(' + str(self.intelligence_bonus) + ')'
        wisdom_string = 'WIS: ' + str(self.wisdom_score) + '(' + str(self.wisdom_bonus) + ')'
        charisma_string = 'CHA: ' + str(self.charisma_score) + '(' + str(self.charisma_bonus) + ')'
        
        l0 = '------------------------------------------------------------------------\n'
        l1 = f"{name_string:<40}{strength_string:>{len(strength_string)}}\n"
        l2 = f"{ac_string:<40}{dexterity_string:>{len(dexterity_string)}}\n"
        l3 = f"{hp_string:<40}{constitution_string:>{len(constitution_string)}}\n"
        l4 = f"{currhp_string:<40}{intelligence_string:>{len(intelligence_string)}}\n"
        l5 = f"{speed_string:<40}{wisdom_string:>{len(wisdom_string)}}\n"
        l6 = f"{type_string:<40}{charisma_string:>{len(charisma_string)}}\n"
        
        final_str = l0 + l1 + l2 + l3 + l4 + l5 + l6
        
        if self.abilities:
            final_str += f'===================ABILITIES=======================\n'
            for ability in self.abilities:
                 final_str += str(ability)
            final_str += f'================================================\n'
                 
        if self.weapons:
            final_str += f'===================WEAPONS=======================\n'
            for weapon in self.weapons:
                final_str += str(weapon)
            final_str += f'================================================\n'
            
        final_str += '------------------------------------------------------------------------\n\n'
        
        return final_str
    
    
    def __repr__(self):
        return str(self)