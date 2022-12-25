import makechar
import roomgen
import pickle
from start import jatka_pelia

def heal(character):
    amount = int(input("How much do you want to heal? 20 gold perh 1 hp"))
    price = amount*20
    print(f"That would be {price} gold for {amount} health Y/N? ")
    choice = input("")

    if choice.upper() == "Y":
        if character.gold < price: 
            # Makes sure that the character has enough money
            print("You don't have enough money to heal")
        else:
            character.health += amount
    else:
        print("No healing then")

def save_and_exit(character):
    with open(f'./characters/{character.name}', 'wb') as file:
        pickle.dump(character, file)
        file.close()
        exit()

def actions(character):
    while True:
        print("You are in town. What do you want to do?")
        print("1 heal\n2 Go to a dungeon\n3 Save and exit")
        actions = {
            1 : heal,
            3 : save_and_exit
        }
        choice = int(input(" "))
        if choice != 2:
            action = actions.get(choice)(character)
        elif choice == 2:
            print("You embark on a dungeon")
            break

if __name__ == "__main__":
    character = jatka_pelia()
    print(character.health)
    character.gold += 300
    actions(character)