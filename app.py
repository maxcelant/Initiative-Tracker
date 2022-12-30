import os
from ability import Ability, Weapon
from creature import Creature
from pool import Pool
from menu import Menu

def load_creatures_from_folder(pool: Pool):
    cwd = os.getcwd()
    file_dir = os.path.join(cwd, 'database')
    for creature_file in os.listdir(file_dir):
        creature_file_path = os.path.join(file_dir, creature_file)
        f = open(creature_file_path, 'r')
        contents = f.readlines()
        name = contents[0].strip()
        ac = int(contents[1])
        hitpoints = int(contents[2])
        speed = int(contents[3])
        type = contents[4].strip()
        strength = int(contents[5])
        dexterity = int(contents[6])
        constitution = int(contents[7])
        intelligence = int(contents[8])
        wisdom = int(contents[9])
        charisma = int(contents[10])
        
        creature = Creature(name=name, 
                          armor_class=ac, 
                          hitpoints=hitpoints, 
                          speed=speed, 
                          type=type, 
                          strength=strength, 
                          dexterity=dexterity,
                          constitution=constitution,
                          intelligence=intelligence,
                          wisdom=wisdom,
                          charisma=charisma)
        
        i = 11
        while(i < len(contents)):
            if(contents[i].strip() == "Ability"):
                ability_name = contents[i+1].strip()
                ability_desc = contents[i+2].strip()
                creature.add_ability(Ability(ability_name, ability_desc))
                i += 3
            elif(contents[i].strip() == "Weapon"):
                weapon_name = contents[i+1].strip()
                weapon_desc = contents[i+2].strip()
                weapon_damage = contents[i+3].strip()
                weapon_atk_bonus = contents[i+4].strip()
                creature.add_weapon(Weapon(weapon_name, weapon_desc, weapon_damage, weapon_atk_bonus))
                i += 5
                
        pool.add(creature)
    print(pool)


def main():
    pool = Pool()
    load_creatures_from_folder(pool)
    Menu(pool)


if __name__ == '__main__':
    main()