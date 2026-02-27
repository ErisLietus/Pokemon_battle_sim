from base_pokemon import Pokemon
import random

class Gardevoir(Pokemon):
    def __init__(self):
        super().__init__("Gardevoir", 200, 85, 50, 50,"Psychic", "Fairy")
        self.moves = {
            "1": ("Moon Blast","Psychic: Channels energy from the moon into a beam", self.moon_blast),
            "2": ("Magic Leaf","Grass: Sends out a magic leaf to attack. never misses.", self.magic_leaf),
            "3": ("Calm Mind","Psychic: A quick hard hitting attack that stuns pokemon.", self.calm_mind),
            "4": ("Drain kiss","Fairy: Lowers the oppenents defence.", self.drain_kiss)
        }
    
    def moon_blast(self, target):
       self.perform_attack(target, self.attack, "Moon Blast", "Psychic")
        
        

    def magic_leaf(self, target):
        self.cannot_miss = 1
        self.perform_attack(target, self.attack, "Magic_leaf", "Grass")
        self.cannot_miss = 0
        

    def calm_mind(self, target):
        if self.attack < self.max_stat_increase_advanced:
            self.attack += 10
            print(f"Gardevoir closes thier eyes and calms thier mind raising its attack. Its attack is now {self.attack}")
            if self.attack == self.max_stat_increase_advanced:
                print(f"Gardevoir's attack cannot be increased anymore")
        else:
            print(f"Gardevoir calms thier mind. But it's attack can not go any higher")
    
    def drain_kiss(self, target):
        heal = self.perform_attack(target, self.attack, "Drain Kiss", "Fairy")
        self.hp += heal 
        if self.hp > self.max_hp:
            self.hp = self.max_hp

        

class Dragonite(Pokemon):
    def __init__(self):
        super().__init__("Dragonite", 220, 60, 60, 45,"Dragon", "Flying")
        self.moves = {
            "1": ("Brutal Swing","Dragon: Swings thier claws at the opponent. Based of attack", self.brutal_swing),
            "2": ("Dragon Rush","Dragon: Rushes at the opponent, lower attack but a chance to stun", self.dragon_rush),
            "3": ("Safeguard","Normal: Makes Pokemon immun to stat changes", self.safeguard),
            "4": ("Hyper Beam ","Normal: Unleashes a powerful beam but stuns the pokemon", self.hyper_beam)
        }
    def brutal_swing(self,target):
        self.perform_attack(target, self.attack, "Brutal Swing", "Dragon")

    def dragon_rush(self, target):
        self.perform_attack(target,self.attack - 10, "Dragon Rush", "Dragon")
        finch = random.randint(1,4)
        if finch == 4:
            print(f"{target.name} is stunned!")
            target.is_stunned = 1

    def safeguard(self, target):
        if self.is_guarded == 1:
            print(f"Dragonite is allready guarded it does nothing")
        else:    
            print(f"Dragonite guards it self")
            self.is_guarded = 1
        

    def hyper_beam(self, target):
        self.perform_attack(target, self.attack + 30, "Hyper Beam", "Normal")
        self.is_stunned = 1
        

class Vanilluxe(Pokemon):
    def __init__(self):
        super().__init__("Vanilluxe", 350, 55, 60, 35,"Ice")
        self.moves = {
            "1": ("Ice beam","Ice: Shoots a beam of ice at the opponent. Based of attack", self.ice_beam),
            "2": ("Chilling water","Water: Raises defence", self.chilling_water),
            "3": ("Flash Cannon", "Steel: Flashes a beam of light at the opponent. Based of lower attack. Has a chance to lower defence", self.flash_cannon),
            "4": ("Blizzard","Ice: Summons a raging blizzard. Based of lower attack. Has a chance to freeze", self.blizzard)
        }

    def ice_beam(self, target):
            self.perform_attack(target, self.attack, "Ice beam", "Ice")

    def chilling_water(self, target):
        if self.defence < self.max_stat_increase_advanced:
            self.defence += 10
            print(f"Vanilluxe Freezes the water in the air creating a coat of ice. Its defence is now {self.defence}")
            if self.defence == self.max_stat_increase_advanced:
                print(f"Vanilluxe's defence cannot go any higher")
        else:
            print(f"Vanilluxe Freezes the water in the air creating a coat of ice. But it's defence can not go any higher")

    def flash_cannon(self,target):
        self.perform_attack(target,self.attack - 10, "Flash Cannon", "Steel")
        lower_defence = random.randint(1,4)
        if lower_defence == 4:
            if target.is_guarded == 1:
                print(f"{target.name} stats cannot be lowered")
            else:
                if target.defence < target.min_stat_decrease:
                    target.defence = target.min_stat_decrease
                    print(f"{target.name} defence cannot be decreased anymore")
                else:
                    target.defence -= 10
                    print(f"{self.name} charmed its opponent! {target.name}'s attack fell!")
                    print(f"{target.name} has {target.attack} attack left!")
        

    def blizzard(self,target):
        self.perform_attack(target,self.attack - 15, "Blizzard", "Ice")
        finch = random.randint(1,3)
        if finch == 3:
            print(f"{target.name} is Frozen!")
            target.is_stunned = 1
        


class Milotic(Pokemon):
    def __init__(self):
        # Balanced Tank/Utility
        super().__init__("Milotic", 220, 55, 65, 45, "Water")
        self.is_guarded = 0
        self.moves = {
            "1": ("Hydro Pump", "Water: High water damage based on attack", self.hydro_pump),
            "2": ("Recover", "Water: Heals a large amount of HP", self.recover),
            "3": ("Aqua Ring", "Water: Grants Safeguard protection", self.aqua_ring),
            "4": ("Water Pulse", "Water: Chance to stun the opponent", self.water_pulse)
        }

    def hydro_pump(self, target):
        self.perform_attack(target, self.attack + 20, "Hydro Pump", "Water")

    def recover(self, target):
        heal = self.max_hp // 3
        self.hp += heal
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print(f"Milotic glows with a beautiful light and heals {heal} HP!")

    def aqua_ring(self, target):
        self.is_guarded = 1
        print("Milotic surrounds itself with a veil of water. Stats cannot be lowered!")

    def water_pulse(self, target):
        self.perform_attack(target, self.attack, "Water Pulse", "Water")
        if random.randint(1, 4) == 4:
            print(f"{target.name} is confused and stunned!")
            target.is_stunned = 1


class Stakataka(Pokemon):
    def __init__(self):
        # Massive Defense, Very Slow
        super().__init__("Stakataka", 180, 75, 110, 5, "Rock", "Steel")
        self.moves = {
            "1": ("Stone Edge", "Rock: Sharp stones deal massive damage", self.stone_edge),
            "2": ("Iron Head", "Steel: Slams its steel body into the target", self.iron_head),
            "3": ("Iron Defense", "Steel: Massively increases defense", self.iron_defense),
            "4": ("Gyro Ball", "Steel: Damage increases the slower Stakataka is", self.gyro_ball)
        }

    def stone_edge(self, target):
        self.perform_attack(target, self.attack + 15, "Stone Edge", "Rock")

    def iron_head(self, target):
        self.perform_attack(target, self.attack + 10, "Iron Head", "Steel")

    def iron_defense(self, target):
        self.defence += 20
        print(f"Stakataka hardens its stone layers. Defense is now {self.defence}!")

    def gyro_ball(self, target):
        # Scaled damage based on being slow
        damage = self.attack + (50 - self.speed)
        self.perform_attack(target, damage, "Gyro Ball", "Steel")


class Volcarona(Pokemon):
    def __init__(self):
        # High Attack and Speed, lower Defense
        super().__init__("Volcarona", 200, 85, 40, 70, "Bug", "Fire")
        self.moves = {
            "1": ("Fiery Dance", "Fire: Flaps wings to deal fire damage and raise attack", self.fiery_dance),
            "2": ("Bug Buzz", "Bug: Vibrates wings to deal bug damage", self.bug_buzz),
            "3": ("Quiver Dance", "Bug: Increases Attack and Speed", self.quiver_dance),
            "4": ("Heat Wave", "Fire: A massive wave of fire that might stun", self.heat_wave)
        }

    def fiery_dance(self, target):
        self.perform_attack(target, self.attack + 10, "Fiery Dance", "Fire")
        self.attack += 5
        print(f"Volcarona's attack rose to {self.attack}!")

    def bug_buzz(self, target):
        self.perform_attack(target, self.attack, "Bug Buzz", "Bug")

    def quiver_dance(self, target):
        self.attack += 10
        self.speed += 10
        print(f"Volcarona dances gracefully! Attack and Speed increased!")

    def heat_wave(self, target):
        self.perform_attack(target, self.attack + 20, "Heat Wave", "Fire")
        if random.randint(1, 5) == 5:
            target.is_stunned = 1
            print(f"{target.name} is stunned by the heat!")