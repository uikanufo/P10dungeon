import pickle

class Player_Character:

    def __init__(self): 
        values = [50, 40, 30]
        def set_attribute(self, attribute):
            nonlocal values
            print(f"What will your {str(attribute)} be? Enter")
            while True:
                for value in values:
                    choicedex = values.index(value)+1
                    print(f"{choicedex} for {value}")
                try:
                    choice = int(input(""))
                    attribute_value = values[choice-1]
                    values.pop(choice-1)    
                except IndexError:
                    print("You can only choose from the values on the list. Enter")
                except:
                    print("I don't think you really understood... let's try again")
                else:
                    break
            return attribute_value


        self.name = input("Name your hero ")
        print("""You can assign the values 50, 40 and 30 to strength, dexterity and intelligence""")
        self.strength = set_attribute(self, "strength")
        self.dexterity = set_attribute(self, "dexterity")
        self.intelligence = set_attribute(self, "intelligence")
        self.food = 20
        self.backpack = []
        self.belt = {slot : "empty" for slot in range(1,6)}
        self.gold = 0
        self.health = 20



            
if __name__ == "__main__":
    Pasi = Player_Character()
    print(Pasi.strength)
    print(Pasi.food, Pasi.backpack)
    print(Pasi.belt)