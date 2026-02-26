from battle_logic import attack_target
import random

class Pokemon:
    def __init__(self, name, pokemon_type, hp, attack, defence, speed):
        self.name = name
        self.type = pokemon_type
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.max_attack = attack
        self.defence = defence
        self.max_defence = defence
        self.speed = speed
        self.max_speed = speed
        self.is_stunned = False
        self.moves = {}  # Subclasses will override this

    def choose_move(self, target):
        print(f"\n{self.name}'s moves:")
        for key, (name, _) in self.moves.items():
            print(f"  {key}. {name}")
    
        choice = input("Choose a move (1-4): ")
    
        if choice in self.moves:
            move_name, move_func = self.moves[choice]
            return move_func(target)
        else:
            print("Invalid choice! Attack missed!")
            return 0

    def random_move(self, target):
        if random.randint(1, 5) == 5:
            print(f"{self.name}'s attack missed!")
            return 0
    
        move_key = random.choice(list(self.moves.keys()))
        move_name, move_func = self.moves[move_key]
        print(f"{self.name} uses {move_name}!")
        return move_func(target)

    
    
    def start_battle(self, target):
        return attack_target(self,target)

        
    

class Pikachu(Pokemon):
    def __init__(self):
        super().__init__("Pikachu", "Electric", 90, 40, 15, 50)
        self.moves = {
            "1": ("Thunder Shock", self.thunder_shock),
            "2": ("Quick Attack", self.quick_attack),
            "3": ("Lighting Tail", self.lighting_tail),
            "4": ("Tail Whip", self.tail_whip)
        }
    
    def thunder_shock(self, target):
        damage = self.attack - target.defence
        target.hp -= damage
        print(f"{self.name} uses Thunder Shock for {damage} damage!")
        

    def quick_attack(self, target):
        damage = self.speed - target.defence
        target.hp -= damage
        print(f"{self.name} uses Quick Attack for {damage} damage!")
        

    def lighting_tail(self,target):
        damage = self.attack + self.speed - target.defence
        target.hp -= damage
        self.is_stunned = True
        print(f"{self.name} uses Lighting Tail for {damage} damage!")
        print(f"{self.name} is stunned!")
    
    def tail_whip(self, target):
        target.defence -= 10
        if target.defence < 0:
            target.defence = 0
        print(f"{self.name} used Tail Whip, lowers {target.name}'s defence!")
        

class Charmander(Pokemon):
    def __init__(self):
        super().__init__("Charmander", "Fire", 100, 35, 20, 35)

class Squirtle(Pokemon):
    def __init__(self):
        super().__init__("Squirtle", "Water", 120, 25, 35, 20)

class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__("Bulbasaur", "Grass", 110, 40, 25, 15)

class Boots(Pokemon):
    def __init__(self):
        super().__init__("Boots", "Psychic", 150, 45, 30, 30)

