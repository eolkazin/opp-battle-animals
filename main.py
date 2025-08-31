import random

class Animals:
    def __init__(self, name, age, life, att):
        self.name = name
        self.age = age
        self.life = life
        self.att = att

    def info(self):
        print(f"name....:{self.name}")
        print(f"age .....:{self.age}")
        print(f"life.....:{self.life}")
        print(f"attack...:{self.att}")
        print("=="*32)

    def fight(self, other):
        if self.att > other.att:
            print(f"{self.name} ganhou")
        elif self.att < other.att:
            print(f"{other.name} ganhou")
        else:
            print("empate")
    
    def battle():
        animals = [Chicken(), Wolf(), Tiger(), Lion()]
        random.shuffle(animals)

        for i in range(0, len(animals), 2):
            a1 = animals[i]
            a2 = animals[i+1]
            print(f"Batalha: {a1.name} vs {a2.name}")
            a1.info()
            a2.info()
            a1.fight(a2)
            print("\n")

class Chicken(Animals):
    def __init__(self):
        super().__init__("Galinha", 2, 50, 25)

class Wolf(Animals):
    def __init__(self):
        super().__init__("Wolf", 4, 75, 45)

class Tiger(Animals):
    def __init__(self):
        super().__init__("Tiger", 4, 75, 45)

class Lion(Animals):
    def __init__(self):
        super().__init__("Lion", 4, 75, 45)


# Chama a batalha
Animals.battle()
