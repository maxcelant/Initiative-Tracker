from collections import OrderedDict
from creature import Creature 

class Tracker:
    def __init__(self):
        s = {i+1:[] for i in range(30)}
        self.initiative_tracker = OrderedDict(s)
    
    
    def add(self, creature: Creature, initiative_score: int):
        self.initiative_tracker[initiative_score].append(creature)
        
    
    def locate(self, creature_identifier):
        for key, list in self.initiative_tracker.items():
            for i, creature in enumerate(list):
                if creature_identifier == creature.id or creature_identifier == creature.nick_name:
                    return (i, creature, list)
        return (None, None, None)
        
    
    def remove(self, creature_identifier):
        index, _, list = self.locate(creature_identifier)
        
        if not index or not list:
            print('Creature not found...')
            return
        
        del list[index]
    
    
    def view(self, creature_identifier):
        _, creature, _ = self.locate(creature_identifier)
        
        if not creature:
            print('Creature not found...')
            return
        
        print(creature)
        
    
    def update_hp(self, creature_identifier, damage):
        _, creature, _= self.locate(creature_identifier)
        
        if not creature:
            print('Creature not found...')
            return
        
        creature.current_hitpoints -= damage
    
    
    def update_condition(self, creature_identifier):
        _, creature, _= self.locate(creature_identifier)
        
        if not creature:
            print('Creature not found...')
            return
        
        