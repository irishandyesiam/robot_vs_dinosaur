from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.dinosaur = Dinosaur("Earl Sinclair")
        self.robot = Robot("Kilroy")
           
    def run_game(self):
        self.display_welcome()
        robo_fighter.attack(dino_fighter) ##this should also be in battle_phrase##
        print(dino_fighter.health) ##this should happen in battle_phrase##

    def display_welcome(self):
        print("Two may enter, one will leave!")
        
    def battle_phrase(self):
        pass

    def display_winner(self):
        pass

dino_fighter = Dinosaur("Earl Sinclair")
robo_fighter = Robot("Kilroy")


robo_fighter.attack(dino_fighter)
print(dino_fighter.health)

dino_fighter.attack(robo_fighter)
print(robo_fighter.health)
# print("find glory in 
# death")