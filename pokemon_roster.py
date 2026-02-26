from base_pokemon import Pokemon
import random

class Pikachu(Pokemon):
    def __init__(self):
        super().__init__("Pikachu", 90, 40, 15, 50,"Electric")
        self.moves = {
            "1": ("Thunder Shock","Shocks opponent damage based of attack.", self.thunder_shock),
            "2": ("Quick Attack","Quickly hits the opponent damage based of speed.", self.quick_attack),
            "3": ("Lighting Tail","A quick hard hitting attack that stuns pokemon.", self.lighting_tail),
            "4": ("Tail Whip","Lowers the oppenents defence.", self.tail_whip)
        }
    
    def thunder_shock(self, target):
       
        self.perform_attack(target, self.attack, "Thunder Shock", "Electric")
        

    def quick_attack(self, target):
        self.perform_attack(target, self.speed, "Quick Attack", "Normal")
        

    def lighting_tail(self, target):
        self.perform_attack(target, self.attack + self.speed, "Lighting Tail", "Electric")
        self.is_stunned = 1
        print(f"{self.name} is stunned!")
    
    def tail_whip(self, target):
        target.defence -= 10
        if target.defence < 0:
            target.defence = 0
        print(f"{self.name} used Tail Whip, lowers {target.name}'s defence!")
        print(f"{target.name} has {target.defence} defence left")
        

class Charmander(Pokemon):
    def __init__(self):
        super().__init__("Charmander", 100, 35, 20, 35,"Fire")
        self.moves = {
            "1": ("Thunder Shock","test", self.thunder_shock),
            "2": ("Quick Attack","test", self.quick_attack),
            "3": ("Lighting Tail","test", self.lighting_tail),
            "4": ("Tail Whip","test", self.tail_whip)
        }
    
    

class Squirtle(Pokemon):
    def __init__(self):
        super().__init__("Squirtle", 120, 25, 35, 20,"Water")
        self.moves = {
            "1": ("Thunder Shock", self.thunder_shock),
            "2": ("Quick Attack", self.quick_attack),
            "3": ("Lighting Tail", self.lighting_tail),
            "4": ("Tail Whip", self.tail_whip)
        }
    
    
class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__("Bulbasaur", 110, 40, 25, 15, "Grass", "Poison")
        self.moves = {
            "1": ("Vine Whip","Hits the opponent with a Vine damage based of attack", self.vine_whip),
            "2": ("Synthesis","Heals Pokemon for 30 HP limited by max HP", self.synthesis),
            "3": ("Razor Leaf","Hits for less damage but has a chance to crit for higher damage", self.razor_leaf),
            "4": ("Growl","Lowers opponents attack", self.growl)
        }

    def vine_whip(self, target):

        self.perform_attack(target, self.attack, "Vine Whip", "Grass")
    

    def synthesis(self, target):
        heal_amount = 30
        self.hp += heal_amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print(f"{self.name} used Synthesis and healed! HP is now {self.hp}")

    def razor_leaf(self,target):
        crit_chance = random.randint(1,2)
        attack_base = self.attack / 2
        if crit_chance == 2:
            crit = self.attack * 2
            print("Critical Hit!")
            self.perform_attack(target, crit, "Razor Leaf", "Grass")
        else:
            self.perform_attack(target,attack_base, "Razor Leaf", "Grass") 

    def growl(self, target):
        target.attack -= 5
        if target.attack < 0:
            target.attack = 0
        print(f"{self.name} growled! {target.name}'s attack fell!")
        print(f"{target.name} has {target.attack} attack left!")
        
    
    

class Boots(Pokemon):
    def __init__(self):
        super().__init__("Boots", 150, 45, 30, 30,"Psychic","Ice")
        self.moves = {
            "1": ("Thunder Shock", self.thunder_shock),
            "2": ("Quick Attack", self.quick_attack),
            "3": ("Lighting Tail", self.lighting_tail),
            "4": ("Tail Whip", self.tail_whip)
        }
    
    