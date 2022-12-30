import os
import copy
import uuid

from pool import Pool
from tracker import Tracker

class Menu:
    
    def __init__(self, pool: Pool):
        self.pool = pool
        self.tracker = Tracker()
        self.run()
        
    def run(self):
        while True:
            os.system('cls')
            self.menu_options()
            choice = input(': ')
            if choice == "1":
                self.add_creature()
            elif choice == "2":
                self.remove_creature()
            elif choice == "3":
                self.view_creature()
            elif choice == "4":
                self.view_collection()
            elif choice == "5":
                self.update_creature()
            elif choice == "6":
                self.view_initiative_tracker()
            
            
    def menu_options(self):
        s0 = '===================COMBAT TRACKER=======================\n'
        s1 = "[1] Add a creature to initiative tracker\n"
        s2 = "[2] Remove creature from initiative tracker\n"
        s3 = "[3] View creature info\n"
        s4 = "[4] Look at creature collection\n"
        s5 = "[5] Update creature\n"
        s6 = "[6] View initiative tracker\n"
        s7 = '========================================================\n'
        all_s = s0 + s1 + s2 + s3 + s4 + s5 + s6 + s7
        print(all_s)
        
    
    def add_creature(self):
        os.system('cls')
        creature_name = input('Enter the creatures name: ')
        if creature_name not in self.pool.creature_pool:
            input('Creature not found in library, Press enter to continue')
            return
         
        creature_nick_name = input('Give the creature a nickname: ')
         
        original = self.pool.creature_pool[creature_name]
        new_creature = copy.copy(original)
        new_creature.set_id(str(uuid.uuid1())[:4])
        new_creature.rename(creature_nick_name)
         
        initiative_roll = input('Enter the creatures initiative: ')
        initiative_roll = int(initiative_roll)
        if initiative_roll > 30 or initiative_roll < 1 or not isinstance(initiative_roll, int):
            print('Invalid input, sorry')
            return
        
        self.tracker.add(new_creature, initiative_roll)
        input('Creature Added! Press enter to continue')
        
    
    def remove_creature(self):
        os.system('cls')
        identifier = input("Enter the creatures's id or nickname: ")
        self.tracker.remove(identifier)
        input('Creature Removed! Press enter to continue')
        
    
    def view_creature(self):
        os.system('cls')
        identifier = input("Enter the creatures's id or nickname: ")
        self.tracker.view(identifier)
        input('Press enter to continue')
        
    
    def view_collection(self):
        os.system('cls')
        print(f'===================COLLECTION=======================\n')
        self.pool.view()
        input('Press enter to return to main menu: ')
        
    
    def update_creature(self):
        os.system('cls')
        identifier = input("Enter the creatures's id or nickname: ")
    
        print("[1] Modify HP\n[2] Add/Remove Condition\n")
        choice = input(': ')
        
        if choice == "1":
            damage_taken = input('Enter damage taken: ')
            self.tracker.update_hp(identifier, int(damage_taken))
            input('Hitpoints Updated! Press enter to return to main menu: ')
            return
        elif choice == "2":
            self.tracker.update_condition(identifier)
            input('Conditions Updated! Press enter to return to main menu: ')
            return
        
    
    def view_initiative_tracker(self):
        os.system('cls')
        print('=========================INITIATIVE TRACKER=========================')
        for key, val in reversed(self.tracker.initiative_tracker.items()):
            for creature in val:
                id = f"({creature.id})"
                nickname = f"'{creature.nick_name}'"
                hp = f"HP: {creature.current_hitpoints} / {creature.hitpoints}"
                print(f"[{key}] {hp:<20} {creature.name} {nickname:>{len(nickname)}} {id:>{len(id)}}")
                
        input('Press enter to return to main menu: ')
        
        