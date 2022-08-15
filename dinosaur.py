class Dinosaur:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 13
       

    def attack(self, robot):
        robot.health -= self.attack_power
        




# print("dinos rule")