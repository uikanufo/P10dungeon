import random

limb_modifiers = {"Head" : 3,
"Back" : 2,
"Torso" : 1,
"Arms" : 0,
"Hands" : 0,
"Main Weapon" : 0,
"Off Weapon" : 0,
"Waist" : 0,
"Legs" : -1,
"Feet" : -1}

dmg_bonus = limb_modifiers.values

tables = []

weapons = ["Sword", "axe", "fists", "1", "2", "3", "4", "5", "6", "7"]
armor = ["Sword", "axe", "fists", "1", "2", "3", "4", "5", "6", "7"]

def table_roll(table, modifier = 0):
    """Basic die roll function for picking things from table"""
    index = random.choice(range(0,9))+modifier
    return table[index]

if __name__ == "__main__":
    print(limb_modifiers.values())