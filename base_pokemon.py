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
        self.is_player_pokemon = False
        self.moves = {}  # Subclasses will override this

    def choose_move(self, target):
        print(f"\n{self.name}'s moves:")
        print("Type 'Stop' to exit game")
        for key, (name, _) in self.moves.items():
            print(f"  {key}. {name}")
    
        choice = input("Choose a move (1-4): ")
    
        if choice in self.moves:
            move_name, move_func = self.moves[choice]
            return move_func(target)
        elif choice == "Stop":
            raise Exception("Exited Match")
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

    def take_damage(self, damage):
        if damage < 5:
            damage = 5
        self.hp -= damage
        return damage
    
    
    def start_battle(self, target):
        return attack_target(self,target)
    
    def perform_attack(self, target, base_damage, move_name):
        if base_damage <= 0:
            print(f"{self.name} is too weak to use {move_name}!")
            return
        
        raw_damage = base_damage - target.defence
        actual_damage = target.take_damage(raw_damage)
        print(f"{self.name} uses {move_name} for {actual_damage} damage!")
        return actual_damage

        
    


