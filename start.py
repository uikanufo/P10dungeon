import makechar
import pickle
import os

def start():
    """Käynnistää pelin, lataa tarvittavat asiat"""

def luo_hahmo():
    """Luo uuden hahmon"""
    character = makechar.Player_Character()
    if os.path.exists('./characters') == False:
        os.mkdir('./characters')
    with open(f'./characters/{character.name}', 'wb') as file:
        pickle.dump(character, file)
        file.close()
    

def jatka_pelia():
    """Valitse hahmo jolla jatkaa"""
    print(os.listdir('./characters/'))
    choice = int(input(""))
    characters = os.listdir('./characters')
    file = open(f'./characters/{characters[choice]}', 'rb')
    return pickle.load(file)
    

if __name__ == "__main__":
    character = jatka_pelia()
    print(character.name)