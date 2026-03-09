from base_pokemon import Pokemon
import random

class Gardevoir(Pokemon):
    def __init__(self):
        super().__init__("Gardevoir", 200, 85, 50, 50,"Psychic", "Fairy")
        self.moves = {
            "1": ("Moon Blast","Psychic: Channels energy from the moon into a beam", self.moon_blast),
            "2": ("Magic Leaf","Grass: Sends out a magic leaf to attack. never misses.", self.magic_leaf),
            "3": ("Calm Mind","Psychic: Raises its own attack and focus.", self.calm_mind),
            "4": ("Drain kiss","Fairy: Steals HP from the opponent.", self.drain_kiss)
        }
    
    def moon_blast(self, target):
       self.perform_attack(target, self.attack, "Moon Blast", "Psychic")

    def magic_leaf(self, target):
        self.cannot_miss = 1
        self.perform_attack(target, self.attack, "Magic_leaf", "Grass")
        self.cannot_miss = 0

    def calm_mind(self, target):
        print(f"Gardevoir closes its eyes and calms its mind...")
        self.modify_stat("attack", 10)
    
    def drain_kiss(self, target):
        heal = self.perform_attack(target, self.attack, "Drain Kiss", "Fairy")
        self.hp += heal 
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print(f"Gardevoir drained energy and healed for {heal}!")

class Dragonite(Pokemon):
    def __init__(self):
        super().__init__("Dragonite", 220, 60, 60, 45,"Dragon", "Flying")
        self.moves = {
            "1": ("Brutal Swing","Dragon: Swings their claws at the opponent.", self.brutal_swing),
            "2": ("Dragon Rush","Dragon: Rushes at the opponent with a chance to stun", self.dragon_rush),
            "3": ("Safeguard","Normal: Makes Pokemon immune to stat changes", self.safeguard),
            "4": ("Hyper Beam ","Normal: Powerful beam that stuns the user", self.hyper_beam)
        }
    def brutal_swing(self,target):
        self.perform_attack(target, self.attack, "Brutal Swing", "Dragon")

    def dragon_rush(self, target):
        self.perform_attack(target, self.attack - 10, "Dragon Rush", "Dragon")
        if random.randint(1, 4) == 4:
            print(f"{target.name} is stunned!")
            target.is_stunned = 1

    def safeguard(self, target):
        if self.is_guarded:
            print(f"Dragonite is already guarded!")
        else:    
            print(f"Dragonite surrounds itself with a protective veil!")
            self.is_guarded = 1

    def hyper_beam(self, target):
        self.perform_attack(target, self.attack + 30, "Hyper Beam", "Normal")
        self.is_stunned = 1
        print("Dragonite needs to recharge!")

class Vanilluxe(Pokemon):
    def __init__(self):
        super().__init__("Vanilluxe", 350, 55, 60, 35,"Ice")
        self.moves = {
            "1": ("Ice beam","Ice: Shoots a beam of ice at the opponent.", self.ice_beam),
            "2": ("Chilling water","Water: Raises defense with a coat of ice", self.chilling_water),
            "3": ("Flash Cannon", "Steel: A beam that may lower enemy defense", self.flash_cannon),
            "4": ("Blizzard","Ice: A raging blizzard that may freeze", self.blizzard)
        }

    def ice_beam(self, target):
        self.perform_attack(target, self.attack, "Ice beam", "Ice")

    def chilling_water(self, target):
        print(f"Vanilluxe freezes the water in the air into armor!")
        self.modify_stat("defence", 10)

    def flash_cannon(self, target):
        self.perform_attack(target, self.attack - 10, "Flash Cannon", "Steel")
        if random.randint(1, 4) == 4:
            if target.is_guarded:
                print(f"{target.name}'s stats cannot be lowered!")
            else:
                target.modify_stat("defence", -10)

    def blizzard(self, target):
        self.perform_attack(target, self.attack - 15, "Blizzard", "Ice")
        if random.randint(1, 3) == 3:
            print(f"{target.name} is Frozen!")
            target.is_stunned = 1

class Milotic(Pokemon):
    def __init__(self):
        super().__init__("Milotic", 220, 55, 65, 45, "Water")
        self.moves = {
            "1": ("Hydro Pump", "Water: High water damage", self.hydro_pump),
            "2": ("Recover", "Water: Heals a large amount of HP", self.recover),
            "3": ("Aqua Ring", "Water: Grants Safeguard protection", self.aqua_ring),
            "4": ("Water Pulse", "Water: Chance to stun the opponent", self.water_pulse)
        }

    def hydro_pump(self, target):
        self.perform_attack(target, self.attack + 20, "Hydro Pump", "Water")

    def recover(self, target):
        heal = self.max_hp // 3
        self.hp = min(self.hp + heal, self.max_hp)
        print(f"Milotic glows with a beautiful light and heals {heal} HP!")

    def aqua_ring(self, target):
        self.is_guarded = 1
        print("Milotic surrounds itself with a veil of water!")

    def water_pulse(self, target):
        self.perform_attack(target, self.attack, "Water Pulse", "Water")
        if random.randint(1, 4) == 4:
            print(f"{target.name} is confused and stunned!")
            target.is_stunned = 1

class Stakataka(Pokemon):
    def __init__(self):
        super().__init__("Stakataka", 180, 75, 110, 5, "Rock", "Steel")
        self.moves = {
            "1": ("Stone Edge", "Rock: Sharp stones deal massive damage", self.stone_edge),
            "2": ("Iron Head", "Steel: Slams body into target", self.iron_head),
            "3": ("Iron Defense", "Steel: Massively increases defense", self.iron_defense),
            "4": ("Gyro Ball", "Steel: Damage based on being slow", self.gyro_ball)
        }

    def stone_edge(self, target):
        self.perform_attack(target, self.attack + 15, "Stone Edge", "Rock")

    def iron_head(self, target):
        self.perform_attack(target, self.attack + 10, "Iron Head", "Steel")

    def iron_defense(self, target):
        print(f"{self.name} hardens it self increases its defence.")
        self.modify_stat("defence", 20)

    def gyro_ball(self, target):
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
        self.modify_stat("attack", 5)

    def bug_buzz(self, target):
        self.perform_attack(target, self.attack, "Bug Buzz", "Bug")

    def quiver_dance(self, target):
        self.modify_stat("attack", 10)
        self.modify_stat("speed", 10)
        print(f"Volcarona dances gracefully! Attack and Speed increased!")

    def heat_wave(self, target):
        self.perform_attack(target, self.attack + 20, "Heat Wave", "Fire")
        if random.randint(1, 5) == 5:
            target.is_stunned = 1
            print(f"{target.name} is stunned by the heat!")