from battle_logic import attack_target
import random
from Type_chart import TYPE_CHART

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

    import random

    def take_damage(self, damage, move_type):
    # 'self' is the Pokemon taking the damage
        multiplier = self.get_effectiveness(move_type)
    
    # Calculate damage with multiplier and variance
        effective_damage = damage * multiplier
        variance = random.uniform(0.85, 1.15)
        final_damage = int(effective_damage * variance)

        if final_damage < 5:
            final_damage = 5
    
        self.hp -= final_damage
        return final_damage

    def get_effectiveness(self, move_type):
        multiplier = 1.0
        type_data = TYPE_CHART.get(self.type)
    
        if type_data:
            if move_type in type_data.get("immunities", []):
                multiplier = 0.0
                print(f"It doesn't affect {self.name}...")
            elif move_type in type_data.get("weaknesses", []):
                multiplier = 2.0
                print("It's super effective!")
            elif move_type in type_data.get("resistances", []):
                multiplier = 0.5
                print("It's not very effective...")
            
        return multiplier
        
       
    
    
    def start_battle(self, target):
        return attack_target(self,target)
    
    def perform_attack(self, target, base_damage, move_name, move_type):
        # 1. Check if the Pokemon is even strong enough to move
        if base_damage <= 0:
            print(f"{self.name} is too weak to use {move_name}!")
            return 0
    
        # 2. Calculate raw damage (Attack vs Defense)
        raw_damage = base_damage - target.defence
    
        # 3. Apply Type Multipliers and Variance in target.take_damage
        actual_damage = target.take_damage(raw_damage, move_type)
    
        # 4. Print the final result
        print(f"{self.name} uses {move_name} for {actual_damage} damage!")
        return actual_damage

        
    


