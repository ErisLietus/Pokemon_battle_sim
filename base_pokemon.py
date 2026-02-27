from battle_logic import attack_target
from battle import battle
import random
from Type_chart import TYPE_CHART
import sys


class Pokemon:
    def __init__(self, name, hp, attack, defence, speed, base_type, second_type = None):
        self.name = name
        self.base_type = base_type
        self.second_type = second_type
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.max_attack = attack
        self.defence = defence
        self.max_defence = defence
        self.speed = speed
        self.max_speed = speed
        self.is_stunned = 0
        self.is_protected = 0
        self.max_stat_increase = 60
        self.min_stat_decrease = 10
        self.is_player_pokemon = False
        self.has_turn = True
        self.moves = {}  # Subclasses will override this

    def choose_move(self, target):
        print(f"\n{self.name}'s moves:")
        print("Type 'run' to flee and stop the game")
        for key, (name,discription, _) in self.moves.items():
            print(f"  {key}. {name}. {discription}")
    
        choice = input("Choose a move (1-4): ")
    
        if choice in self.moves:
            move_name, move_des, move_func = self.moves[choice]
            if random.randint(1, 5) == 5:
                print(f"{self.name}'s attack missed!")
                return 0
            return move_func(target)
        elif choice.lower() == "run":
            print(f"{self.name} ran away. .... Coward!")
            sys.exit()
        else:
            print("Invalid choice! Attack missed!")
            return 0

    def random_move(self, target):
        if random.randint(1, 5) == 5:
            print(f"{self.name}'s attack missed!")
            return 0
    
        move_key = random.choice(list(self.moves.keys()))
        move_name,move_des, move_func = self.moves[move_key]
        print(f"{self.name} uses {move_name}!")
        return move_func(target)

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
        total_multiplier = 1.0
        # Put both types in a list and filter out None
        my_types = [t for t in [self.base_type, self.second_type] if t is not None]

        for t in my_types:
            type_data = TYPE_CHART.get(t)
            if type_data:
                if move_type in type_data.get("immunities", []):
                    total_multiplier *= 0.0
                elif move_type in type_data.get("weaknesses", []):
                    total_multiplier *= 2.0
                elif move_type in type_data.get("resistances", []):
                    total_multiplier *= 0.5

        # Give the player feedback based on the final result
        if total_multiplier > 1.0:
            print("It's super effective!")
        elif 0 < total_multiplier < 1.0:
            print("It's not very effective...")
        elif total_multiplier == 0:
            print(f"It doesn't affect {self.name}...")

        return total_multiplier
        
    
    def start_battle(self, target):
        return attack_target(self, target)
    
    def perform_attack(self, target, base_damage, move_name, move_type):
        # 1. Check if the Pokemon is even strong enough to move
        if base_damage <= 0:
            print(f"{self.name} is too weak to use {move_name}!")
            return 0
    
        # 2. Calculate raw damage (Attack vs Defense)
        raw_damage = base_damage - target.defence
    
        # 3. Apply Type Multipliers and Variance in target.take_damage
        if target.is_protected == 1:
            actual_damage = 0
            print(f"{target.name} is protected")
            target.is_protected = 0
        else:    
            actual_damage = target.take_damage(raw_damage, move_type)
    
        # 4. Print the final result
        print(f"{self.name} uses {move_name} for {actual_damage} damage!")
        return actual_damage

        
    


