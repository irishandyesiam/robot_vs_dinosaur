from weapon import Weapon

class Robot:
    
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_weapon = Weapon("rocket punch", 5)
      

    def attack(self, dinosaur):
        dinosaur.health -= self.attack_weapon.attack_power
        
attack_weapon = Weapon("rocket punch", 5)

 
# print("you will be assimulated")