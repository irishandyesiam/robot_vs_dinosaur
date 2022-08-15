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
        dino_fighter.attack(robo_fighter)
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

# attack_weapon = Weapon("Rocket punch", 5)
# attack_weapon1 = Weapon("Rocket punch", 5)
# attack_weapon2 = Weapon("Super Flower Blood Moon Attack", 6)
# attack_weapon3 = Weapon("ATATATATATATATATATATATATATATATATATATATATATATATATATATATATATATATA", 17)

# attack_weapon1 = Weapon("rocket punch", 5)
# attack_weapon2 = Weapon("Super Flower Blood Moon Attack", 6)
# attack_weapon3 = Weapon("ATATATATATATATATATATATATATATATATATATATATATATATATATATATATATATATA", 17)
# print("find glory in 
# death")