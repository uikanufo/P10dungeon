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
    def __init__(self, position:tuple):
        index = random.randint(0,2)
        self.colour = self.parametres[index][0]
        self.exits = self.parametres[index][1]
        self.searched = False
        self.position = tuple(position)

    def search(self):
        if self.searched == False:
            self.searched = True
            print("Looooot!")
        else:
            print("Ahne peruna :P")

    def position(self):
        return self.position()
    


class Ungeon:
    def __init__(self):
        startroom = Room((0, 0,))
        startroom.searched = True
        self.rooms = [startroom]
        self.player_position = [0, 0]
        self.roomdex = [0, 0] 

#    def current_room(self):
#        
#        positions = []
#        for room in self.rooms:
#            positions.append(room.position())
        




    def add_room(self):
        self.roomdex[1] += 1 
        kaali = Room(self.roomdex)
        self.rooms.append(kaali)

    def room_positions(self):
        positions = []
        for room in self.rooms:
            positions.append(room.position)
        return positions

    def current_room(self):
        positions = self.room_positions()
        posindex = positions.index(tuple(self.player_position))
        return self.rooms[posindex]

    def player_move(self):
        suunnat = {"N" : 1, "S" : -1}
        direction = input("Where do you want to move? \nN for north \nS for south \n")
        self.player_position[1] += suunnat.get(direction)

        if self.player_position[1] not in range(self.roomdex[1]+1):
            self.add_room()
        
    def search(self):
        self.current_room().search()


    
    def choose_action(self):
        actions = {"1" : self.player_move,
                    "2" : self.search}
        print("1 Move\n2 Search")
        if self.current_room().searched != True:
            print("Current room is not searched")
        else:
            print("The current room has been searched")
        choice = input("Choose your action: ")
        choice = actions.get(choice)()



if __name__ == "__main__":
    test = Ungeon()
    while True:
        test.choose_action()
        print(test.room_positions())

