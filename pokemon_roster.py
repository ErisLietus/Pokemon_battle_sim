from base_pokemon import Pokemon
import random

class Pikachu(Pokemon):
    def __init__(self):
        super().__init__("Pikachu", 90, 40, 15, 50,"Electric")
        self.moves = {
            "1": ("Dash","Normal:Increases Pikachus speed.", self.Dash),
            "2": ("Quick Attack","Normal:Quickly hits the opponent damage based of speed.", self.quick_attack),
            "3": ("Lighting Tail","Electric: A quick hard hitting attack that stuns pokemon.", self.lighting_tail),
            "4": ("Tail Whip","Normal: Lowers the oppenents defence.", self.tail_whip)
        }
    
    def Dash(self, target):
       
        if self.speed < self.max_stat_increase_basic:
            self.speed += 5
            print(f"Pikachu dashed around the arena it increased it's speed to {self.speed}")
            if self.speed == self.max_stat_increase_basic:
                print(f"Pikachu's speed cannnot go any higher")
        else:
            print(f"Pikachu's dashed around the arena but its speed can not go any higher")
        

    def quick_attack(self, target):
        self.perform_attack(target, self.speed, "Quick Attack", "Normal")
        

    def lighting_tail(self, target):
        self.perform_attack(target, self.attack + self.speed, "Lighting Tail", "Electric")
        self.is_stunned = 1
        print(f"{self.name} is stunned!")
    
    def tail_whip(self, target):
        target.defence -= 5
        if target.defence < 0:
            target.defence = 0
        print(f"{self.name} used Tail Whip, lowers {target.name}'s defence!")
        print(f"{target.name} has {target.defence} defence left")
        

class Charmander(Pokemon):
    def __init__(self):
        super().__init__("Charmander", 100, 35, 20, 35,"Fire")
        self.moves = {
            "1": ("Ember","Fire: Throws a flame at the opponent. Based of attack", self.ember),
            "2": ("Dragon Rage","Dragon: Breaths wild fire at the opponent, ingores defence but takes recoil damage", self.dragon_rage),
            "3": ("Cheer","Normal: Cheers it self on. Increases attack", self.cheer),
            "4": ("Scary Face","Normal: Pulls a scary face at the opponent. Lowers thier speed", self.scary_face)
        }
    def ember(self,target):
        self.perform_attack(target, self.attack, "Ember", "Fire")

    def dragon_rage(self, target):
        temp = target.defence
        target.defence = 0
        self.perform_attack(target, self.attack + 15, "Dragon Rage", "Dragon")
        target.defence = temp
        self.hp -= 15
        print(f"{self.name} recoiled and damaged it self. It has{self.hp}HP left")

    def cheer(self, target):
        if self.attack < self.max_stat_increase_basic:
            self.attack += 5 
            print(f"Charmander cheered it self on raising its attack. Its attack is now {self.attack}")
            if self.attack == self.max_stat_increase_basic:
                print(f"Charmanders attack cannot be increased anymore")
        else:
            print(f"Charmander cheered it self on. But it's attack can not go any higher")

    def scary_face(self, target):
        target.speed -= 5
        print(f"{self.name} made a scary face. {target.name}'s speed fell!")
        print(f"{target.name} has {target.speed} speed left!")
        if target.speed < target.min_stat_decrease:
            target.speed = target.min_stat_decrease
            print(f"{target.name} speed cannot be decreased anymore")

class Squirtle(Pokemon):
    def __init__(self):
        super().__init__("Squirtle", 120, 25, 35, 20,"Water")
        self.moves = {
            "1": ("Water Gun","Water: Shoots water at the opponent based of attack", self.water_gun),
            "2": ("Withdraw","Normal: Raises defence", self.withdraw),
            "3": ("Protect", "Normal: Protects it self for one turn", self.protect),
            "4": ("Skull Bash","Normal: Goes into its shell and Rams into the opponent", self.skull_bash)
        }

    def water_gun(self, target):
            self.perform_attack(target, self.attack, "Water Gun", "Water")

    def withdraw(self, target):
        if self.defence < self.max_stat_increase_basic:
            self.defence += 5 
            print(f"Squirte withdraws into its shell increasing its defence. Its defence is now {self.defence}")
            if self.defence == self.max_stat_increase_basic:
                print(f"Squirtes defence cannot be increased anymore")
        else:
            print(f"Squirte withdraws into its shell. But it's defence can not go any higher")

    def protect(self,target):
        self.is_protected = 1
        print(f"Squirtle hid inside its shell. It is protected for one turn")

    def skull_bash(self,target):
        self.perform_attack(target, self.defence, "Skull bash", "Normal")
        

    
    
class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__("Bulbasaur", 110, 40, 25, 15, "Grass", "Poison")
        self.moves = {
            "1": ("Vine Whip","Grass: Hits the opponent with a Vine damage based of attack", self.vine_whip),
            "2": ("Synthesis","Grass: Heals Pokemon for 30 HP limited by max HP", self.synthesis),
            "3": ("Razor Leaf","Grass: Hits for less damage but has a chance to crit for higher damage", self.razor_leaf),
            "4": ("Growl","Normal: Lowers opponents attack", self.growl)
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
        print(f"{self.name} growled! {target.name}'s attack fell!")
        print(f"{target.name} has {target.attack} attack left!")
        if target.attack < target.min_stat_decrease:
            target.attack = target.min_stat_decrease
            print(f"{target.name} defence cannot be decreased anymore")

class Eevee(Pokemon):
    def __init__(self):
        super().__init__("Eevee", 110, 40, 20, 25, "Normal")
        self.moves = {
            "1": ("Bite","Dark: Bits the opponent", self.bite),
            "2": ("Disarming Voice","Fairy: attacks for less damage but hits regardless of protected state", self.disarming_voice),
            "3": ("Swift","Normal: Hits three times with a chance to crit or do less damage", self.swift),
            "4": ("Charm","Normal: Lowers opponents attack", self.charm)
        }

    def bite(self, target):

        self.perform_attack(target, self.attack, "Bite", "Dark")
    

    def disarming_voice(self, target):
        target.is_protected = 0
        temp = target.attack - 5
        self.perform_attack(target, temp, "Disarming voice", "Fairy")

    def swift(self,target):
        print(f"{self.name} unleashed a flurry of stars!")
    # Loop 3 times for 3 separate hits
        for i in range(3):
        # Calculate if this specific hit crits
            if random.randint(1, 4) == 4:
                print("Critical Hit!")
                damage = self.attack // 1.5 * 2
            else:
                damage = self.attack // 2
        
        self.perform_attack(target, damage, "Swift", "Normal")

    def charm(self, target):
        target.attack -= 5
        print(f"{self.name} charmed its opponent! {target.name}'s attack fell!")
        print(f"{target.name} has {target.attack} attack left!")
        if target.attack < target.min_stat_decrease:
            target.attack = target.min_stat_decrease
            print(f"{target.name} attack cannot be decreased anymore")

class Snorlax(Pokemon):
    def __init__(self):
        # High HP, Low Speed, Decent Attack/Defense
        super().__init__("Snorlax", 160, 50, 40, 5, "Normal")
        self.moves = {
            "1": ("Body Slam", "Normal: Slams its heavy body into the opponent.", self.body_slam),
            "2": ("Rest", "Normal: The Snorlax takes a nap, healing but becoming stunned.", self.rest),
            "3": ("Yawn", "Normal: A huge yawn that lowers the opponent's speed.", self.yawn),
            "4": ("Amnesia", "Normal: Forgets its troubles to raise its own defense.", self.amnesia)
        }

    def body_slam(self, target):
        self.perform_attack(target, self.attack + 10, "Body Slam", "Normal")

    def rest(self, target):
        # The ultimate healing move
        self.hp += 50
        if self.hp >= self.max_hp:
            self.hp = self.max_hp
        self.is_stunned = 1
        print(f"The Snorlax {self.name} fell asleep and recovered all HP!")
        print(f"{self.name} is stunned and cannot move next turn!")

    def yawn(self, target):
        target.speed -= 10
        if target.speed < target.min_stat_decrease:
            target.speed = target.min_stat_decrease
        print(f"{self.name} let out a massive yawn! {target.name} is feeling drowsy and its speed fell!")

    def amnesia(self, target):
        if self.defence < self.max_stat_increase_basic:
            self.defence += 10
            print(f"{self.name} used Amnesia! Its defense rose to {self.defence}!")
        else:
            print(f"{self.name} already forgot everything it could!")
        
     

class Boots(Pokemon):
    def __init__(self):
        # High stats for a final boss encounter
        super().__init__("Boots", 150, 40, 30, 30, "Psychic", "Ice")
        self.moves = {
            "1": ("Enchanted Wisdom","Psychic: Psychic blasts the opponent", self.enchanted_wisdom),
            "2": ("Crystal Clarity","Psychic:Showers the opponent with icy shards", self.crystal_clarity),
            "3": ("Debug","Normal:Lowers the opponents defence", self.debug),
            "4": ("Deep Freeze", "Ice: Freezes the opponent for high damage is left stunned", self.deep_freeze)
        }

    def enchanted_wisdom(self, target):
        # A standard powerful Psychic attack
        self.perform_attack(target, self.attack , "Enchanted Wisdom", "Psychic")

    def crystal_clarity(self, target):
        # An Ice attack that scales with both Speed and Attack
        damage = (self.attack + self.speed) // 1.5
        self.perform_attack(target, damage, "Crystal Clarity", "Ice")

    def debug(self, target):
        # Lowers the player's defense significantly, making them vulnerable
        target.defence -= 10
        if target.defence < target.min_stat_decrease:
            target.defence = target.min_stat_decrease
        print(f"Boots uses Debug! {target.name}'s defense dropped by 10 points!")

    def deep_freeze(self, target):
        # A "finisher" move: Massive damage, but stuns the user
        self.perform_attack(target, self.attack * 2, "Deep Freeze", "Ice")
        self.is_stunned = 1 
        print("Boots is exhausted from the absolute zero temperature!")
    
    