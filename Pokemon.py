from battle_logic import attack_target

class Pokemon:
    def __init__(self, name, pokemon_type, hp, attack, defence, speed):
        self.name = name
        self.type = pokemon_type
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defence = defence
        self.speed = speed
        self.moves = {}  # Subclasses will override this

    def choose_move(self, target):
        print(f"\n{self.name}'s moves:")
        for key, (name, _) in self.moves.items():
            print(f"  {key}. {name}")
        
        choice = input("Choose a move (1-4): ")
        
        if choice in self.moves:
            move_name, move_func = self.moves[choice]
            move_func(target)
        else:
            print("Invalid choice! Attack missed!")
        
    
    
    def start_battle(self, target):
        return attack_target(self,target)

        
    

class Pikachu(Pokemon):
    def __init__(self):
        super().__init__("Pikachu", "Electric", 90, 40, 15, 50)

    def electric_tail(self, target):
        damage = self.attack + self.speed - target.defence
        target.hp -= damage
        print(f"{self.name} uses Electric Tail on {target.name} for {damage} damage!")

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

