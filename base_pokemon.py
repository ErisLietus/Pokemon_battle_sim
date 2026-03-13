from battle_logic import attack_target
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
        self.max_stat_increase_basic = 60
        self.min_stat_decrease = 10
        self.max_stat_increase_advanced = 120
        self.cannot_miss = 0
        self.is_guarded = 0
        self.is_player_pokemon = False
        self.has_turn = True
        self.moves = {}  # Subclasses will override this

    def choose_move(self, target):
        # 1. Show the moves
        print(f"\n{self.name}'s moves:")
        for key, move_obj in self.moves.items():
            print(f"  {key}. {move_obj.name}: {move_obj.description}")
        print("Type 'run' to flee.")

        # 2. The Loop for Valid Input
        while True:
            choice = input("Choose a move (1-4): ").strip().lower()

            if choice == "run":
                print(f"{self.name} ran away...Tsss, Coward!")
                sys.exit()

            if choice in self.moves:
                # We found a valid move! Run it and exit the loop.
                move_obj = self.moves[choice]
                return move_obj.execute(self, target)
            
            # If we get here, the input was bad
            print(f"Invalid choice! Please pick a number from: {', '.join(self.moves.keys())}")
        

    def random_move(self, target): 
        move_key = random.choice(list(self.moves.keys()))
        move_obj = self.moves[move_key]
        return move_obj.execute(self,target)

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
        
        # 2. Calculate raw damage (Attack vs Defense)
        raw_damage = base_damage - target.defence
    
        # 3. Apply Type Multipliers and Variance in target.take_damage
        if target.is_protected == 1:
            actual_damage = 0
            print(f"{target.name} is protected")
            target.is_protected = 0
        else:
            if random.randint(1, 5) == 5:
                if self.cannot_miss == 1:
                   actual_damage = target.take_damage(raw_damage, move_type) 
                else:
                    print(f"{self.name}'s attack missed!")
                    actual_damage = 0
                
            else:    
                actual_damage = target.take_damage(raw_damage, move_type)
    
        # 4. Print the final result
        print(f"{self.name} uses {move_name} for {actual_damage} damage!")
        return actual_damage
    
    def modify_stat(self, stat_name, amount):
        if amount > 0:
            limit = self.max_stat_increase_advanced
        else:
            limit = self.min_stat_decrease

        current_val = getattr(self, stat_name)
        
        if (amount > 0 and current_val >= limit) or (amount < 0 and current_val <= limit):
            print(f"{self.name}'s {stat_name} cannot go any {'higher' if amount > 0 else 'lower'}!")
            return

        new_val = current_val + amount
        if amount > 0:
            new_val = min(new_val, limit)
        else:
            new_val = max(new_val, limit)

        setattr(self, stat_name, new_val)
        direction = "rose" if amount > 0 else "fell"
        print(f"{self.name}'s {stat_name} {direction} to {new_val}!")

    

        
    


