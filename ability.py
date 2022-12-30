from dataclasses import dataclass

'''
    - Abilities can be anything from spells to weapons
'''

@dataclass
class Ability:
    name: str = "Default Ability"
    description: str = ""
    
    def __str__(self):
        l1 = f'Name: {self.name}\n'
        l2 = f'Description: {self.description}\n'
        return l1 + l2
    
    def __repr__(self):
        return str(self)
    
    
@dataclass
class Weapon(Ability):
    damage: str = ""
    attack_bonus: str = ""
    
    def __str__(self):
        
        l1 = f'Name: {self.name}\n'
        l2 = f'Description: {self.description}\n'
        l3 = f'Attack: 1d20{self.attack_bonus}\n'  
        l4 = f'Damage: {self.damage}\n'
        return l1 + l2 + l3 + l4
    
    def __repr__(self):
        return str(self)