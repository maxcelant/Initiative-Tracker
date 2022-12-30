from collections import defaultdict
from creature import Creature

class Pool:
    
    def __init__(self):
        self.creature_pool = defaultdict(Creature)
       
    # Add a creature to the pool 
    def add(self, creature: Creature):
        self.creature_pool[creature.name] = creature
        
    
    def view(self):
        for name, _ in self.creature_pool.items():
            print(name)
        
    
    def __str__(self):
        creatures_str = []
        for key in self.creature_pool.keys():
            c = self.creature_pool[key]
            creatures_str.append(str(c))
        return "".join(creatures_str)
            
            
    def __repr__(self):
        return str(self)