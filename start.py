import makechar
import pickle
import os


def luo_hahmo():
    """Creates and stores a character object"""
    player = makechar.Player_Character()
    if os.path.exists('./characters') == False:
        os.mkdir('./characters')
    with open(f'./characters/{player.name}', 'wb') as file:
        pickle.dump(player, file)
        file.close()
    

def jatka_pelia():
    """Loads and unpickles a character object, and returns said object"""
    directory = os.listdir('./characters/')
    print("Choose your character:")
    for character in directory:
        print((directory.index(character))+1, character)
    choice = int(input(""))-1
    file = open(f'./characters/{directory[choice]}', 'rb')
    return pickle.load(file)


def menu():
    while True:
        actions = {1 : luo_hahmo,
        3 : exit}
        print("""Welcome to P10dungeon!
    1 Make a new character
    2 Continue a character
    3 Exit""")
        choice = int(input(""))
        if choice == 2:
            break
        else:
            actions.get(choice)()

if __name__ == "__main__":
    character = jatka_pelia()
    print(character.name)
