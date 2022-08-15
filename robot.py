from weapon import Weapon

class Robot:
    
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_weapon = Weapon("",0)

    def select_weapon(self):
        # rocket_punch = Weapon("Rocket Punch", 5)
        # super_fbma = Weapon("Super Flower Blood Moon Attack", 6)
        # atatatata = Weapon("ATATATATATATATATATATATATATATATATATATATATATATATATATATATATATATATA", 17)
        weapon_select = False
        while weapon_select == False:
            user_input = input("Select Robot special attack. Please enter, Rocket Punch, Moon Attack, Kenshiro.")
            if user_input == "Rocket Punch":
                self.attack_weapon = Weapon("Rocket Punch", 5)
                print("Rocket punch, engaged.")
                weapon_select = True
            elif user_input == "Moon Attack":
                self.attack_weapon = Weapon("Super Flower Blood Moon Attack", 6)
                print("Moon Attack, engaged.")
                weapon_select = True
            elif user_input == "Kenshiro":
                self.attack_weapon = Weapon("ATATATATATATATATATATATATATATATATATATATATATATATATATATATATATATATA", 17)
                print("Kenshiro, engaged.")
                weapon_select = True
            else:
                weapon_select = False
                print("Please resubmit weapon choice.")  
            

    def attack(self, dinosaur):
        # self.select_weapon()
        dinosaur.health -= self.attack_weapon.attack_power
        print(f"{self.name} attacks {dinosaur.name} with {self.attack_weapon.name}!")
        print(f"{dinosaur.name} is damaged and now health is at {dinosaur.health}.")
      

# # attack_weapon = Weapon("Rocket Punch", 5)
# rocket_punch = Weapon("Rocket Punch", 5)
# super_fbma = Weapon("Super Flower Blood Moon Attack", 6)
# Kenshiro = Weapon("ATATATATATATATATATATATATATATATATATATATATATATATATATATATATATATATA", 17)

# ("Rocket Punch", 5)
# ("Super Flower Blood Moon Attack", 6)
# ("ATATATATATATATATATATATATATATATATATATATATATATATATATATATATATATATA", 17)
# print("you must choose, but choose wisely")

# print("you will be assimulated")