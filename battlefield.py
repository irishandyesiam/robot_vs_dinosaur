from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.dinosaur = Dinosaur("Earl Sinclair")
        self.robot = Robot("Kilroy")
           
    def run_game(self):
        self.display_welcome()
        self.battle_phrase()
        

    def display_welcome(self):
        print("What happens when you force a dinosaur to defend itself against a mindless killing machine? Find out today at THE KILLING FIELD. Two may enter, one will leave!")
        
    def battle_phrase(self):
        robo_fighter.attack(dino_fighter) 
        print(f"{robo_fighter.name} attacks {dino_fighter.name} with {robo_fighter.attack_weapon}")
        print(f"{dino_fighter.name} is damaged and now health is at {dino_fighter.health}.")
        dino_fighter.attack(robo_fighter)
        print(f"{dino_fighter.name} attacks {robo_fighter.name}")
        print(f"{robo_fighter.name} is damaged and now health is at {robo_fighter.health}.")
        self.display_winner()
    def display_winner(self):
        if dino_fighter.health == 0:
            print(f"{robo_fighter.name} is victorious!")
        elif robo_fighter.health == 0:
            print(f"{dino_fighter.name} is victorious!")
        else:
            self.battle_phrase()    
    
dino_fighter = Dinosaur("Earl Sinclair")
robo_fighter = Robot("Kilroy")

print(robo_fighter.attack_weapon)
# print("find glory in 
# death")