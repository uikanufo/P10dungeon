class monster:
    def __init__(self, properties) -> None:
        self.Name = properties[0]
        self.Attack_value = int(properties[1])
        self.Defense = int(properties[2])
        self.Damage = int(properties[3])
        self.HP = int(properties[4])
        self.Loot = properties[5]
        self.Other_traits = properties[6]

def fetch(file):
    list = []
    for line in file:
        line = line.strip("\n") 
        line = line.split(",")
        list.append(line)
    return list

with open("./Monsters.csv") as file:
    print(fetch(file))

def make_table(file):
    type = []
    with open(file) as source:
        type.append(fetch(source))
    return type

print(make_table("./Monsters.csv"))