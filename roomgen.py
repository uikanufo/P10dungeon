import random
import time

def heita_noppaa():
    print("heitetään noppaa...")
    time.sleep(0.1)
    # random numero juttu
    numero = random.randint(1, 10)
    print("nopasta tuli", numero)
    return numero

perunavero = []

class Room: 
    parametres = [# colour, open exits
    ("red", 3,),
    ("yellow", 2,),
    ("green", 1) ]
    def __init__(self):
        index = random.randint(0,2)
        self.colour = self.parametres[index][0]
        self.exits = self.parametres[index][1]
        self.searched = False
    def search(self):
        if self.searched == False:
            self.searched = True
            print("Looooot!")
        else:
            print("Ahne peruna :P")

class Ungeon:
    def __init__(self):
        self.rooms = []
    def add_room(self):
        kaali = Room()
        self.rooms.append(kaali)


peruna = Ungeon()
peruna.add_room()
print(peruna.rooms)

