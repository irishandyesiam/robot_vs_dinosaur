from weapon import Weapon

class Robot:
    
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_weapon = Weapon("", 0)

    def select_weapon(self, name):
        attack_weapon1 = Weapon("Rocket Punch", 5)
        attack_weapon2 = Weapon("Super Flower Blood Moon Attack", 6)
        attack_weapon3 = Weapon("ATATATATATATATATATATATATATATATATATATATATATATATATATATATATATATATA", 17)
        input("Select Robot special attack.")
        if name == attack_weapon1:
            attack_weapon1 = Weapon("Rocket Punch", 5)
        elif name == attack_weapon2:
            attack_weapon2 = Weapon("Super Flower Blood Moon Attack", 6)
        elif name == attack_weapon3:
            attack_weapon3 = Weapon("ATATATATATATATATATATATATATATATATATATATATATATATATATATATATATATATA", 17)
            print("Please resubmit weapon choice.")  

    def attack(self, dinosaur):
        self.select_weapon(Weapon)
        dinosaur.health -= self.attack_weapon.attack_power
        print(f"{self.name} attacks {dinosaur.name} with {self.attack_weapon.name}!")
        print(f"{dinosaur.name} is damaged and now health is at {dinosaur.health}.")
      



   

# attack_weapon = Weapon("Rocket Punch", 5)
# attack_weapon1 = Weapon("Rocket Punch", 5)
# attack_weapon2 = Weapon("Super Flower Blood Moon Attack", 6)
# attack_weapon3 = Weapon("ATATATATATATATATATATATATATATATATATATATATATATATATATATATATATATATA", 17)

# ("Rocket Punch", 5)
# ("Super Flower Blood Moon Attack", 6)
# ("ATATATATATATATATATATATATATATATATATATATATATATATATATATATATATATATA", 17)
# print("you must choose, but choose wisely")

# print("you will be assimulated")