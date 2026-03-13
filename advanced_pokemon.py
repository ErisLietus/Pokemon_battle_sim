from base_pokemon import Pokemon
from move import Move

class Gardevoir(Pokemon):
    def __init__(self):
        super().__init__("Gardevoir", 200, 85, 50, 50, "Psychic", "Fairy")
        self.moves = {
            "1": Move(
                "Psychic beam from the moon", "Gardevoir channels lunar energy!", 
                "Moon Blast", "Psychic", "attack", 0
            ),
            "2": Move(
                "Attack that never misses", "Gardevoir sends out magical leaves!", 
                "Magic Leaf", "Grass", "attack", 0, 
                effects=["never misses"]
            ),
            "3": Move(
                "Raises attack and focus", "Gardevoir closes its eyes and calms its mind...", 
                "Calm Mind", "Psychic", "attack", 0, 
                is_attack=False, stat_to_fix=["attack"], effect_value=10, target_self=True
            ),
            "4": Move(
                "Steals HP from the opponent", "Gardevoir drains energy with a kiss!", 
                "Drain Kiss", "Fairy", "attack", 0, 
                effects=["heal"] # Our Move class heal uses damage dealt as the amount!
            )
        }

class Dragonite(Pokemon):
    def __init__(self):
        super().__init__("Dragonite", 220, 60, 60, 45, "Dragon", "Flying")
        self.moves = {
            "1": Move(
                "Standard dragon damage", "Dragonite swings its mighty claws!", 
                "Brutal Swing", "Dragon", "attack", 0
            ),
            "2": Move(
                "Damage with chance to stun", "Dragonite rushes at the opponent!", 
                "Dragon Rush", "Dragon", "attack", -10, 
                effects=["stun"]
            ),
            "3": Move(
                "Immune to stat changes", "Dragonite surrounds itself with a protective veil!", 
                "Safeguard", "Normal", "attack", 0, 
                is_attack=False, effects=["shield"]
            ),
            "4": Move(
                "Massive beam but stuns user", "Dragonite fires a powerful beam!", 
                "Hyper Beam", "Normal", "attack", 30, 
                effects=["stun"], target_self=True
            )
        }

class Vanilluxe(Pokemon):
    def __init__(self):
        super().__init__("Vanilluxe", 350, 55, 60, 35, "Ice")
        self.moves = {
            "1": Move(
                "Standard ice damage", "Vanilluxe shoots a beam of ice!", 
                "Ice Beam", "Ice", "attack", 0
            ),
            "2": Move(
                "Raises defense", "Vanilluxe freezes the water in the air into armor!", 
                "Chilling Water", "Water", "attack", 0, 
                is_attack=False, stat_to_fix=["defence"], effect_value=10, target_self=True
            ),
            "3": Move(
                "Chance to lower enemy defense", "Vanilluxe fires a metallic beam!", 
                "Flash Cannon", "Steel", "attack", -10, 
                stat_to_fix=["defence"], effect_value=-10, target_self=False
            ),
            "4": Move(
                "High damage with stun chance", "A raging blizzard surrounds the arena!", 
                "Blizzard", "Ice", "attack", -15, 
                effects=["stun"]
            )
        }

class Milotic(Pokemon):
    def __init__(self):
        super().__init__("Milotic", 220, 55, 65, 45, "Water")
        self.moves = {
            "1": Move(
                "High water damage", "Milotic blasts a high-pressure stream of water!", 
                "Hydro Pump", "Water", "attack", 20
            ),
            "2": Move(
                "Heals a large amount of HP", "Milotic glows with a beautiful light!", 
                "Recover", "Water", "attack", 0, 
                is_attack=False, effects=["heal"], effect_value=70, target_self=True
            ),
            "3": Move(
                "Grants protection", "Milotic surrounds itself with a veil of water!", 
                "Aqua Ring", "Water", "attack", 0, 
                is_attack=False, effects=["shield"]
            ),
            "4": Move(
                "Chance to stun", "Milotic pulses water at the opponent!", 
                "Water Pulse", "Water", "attack", 0, 
                effects=["stun"]
            )
        }

class Stakataka(Pokemon):
    def __init__(self):
        super().__init__("Stakataka", 180, 75, 110, 5, "Rock", "Steel")
        self.moves = {
            "1": Move(
                "Sharp stones deal massive damage", "Stakataka creates a ring of sharp stones!", 
                "Stone Edge", "Rock", "attack", 15
            ),
            "2": Move(
                "Standard steel damage", "Stakataka slams its heavy body into the target!", 
                "Iron Head", "Steel", "attack", 10
            ),
            "3": Move(
                "Massively increases defense", "Stakataka hardens its stone blocks!", 
                "Iron Defense", "Steel", "attack", 0, 
                is_attack=False, stat_to_fix=["defence"], effect_value=20, target_self=True
            ),
            "4": Move(
                "Damage based on being slow", "Stakataka spins its heavy body!", 
                "Gyro Ball", "Steel", "attack", 45
            )
        }

class Volcarona(Pokemon):
    def __init__(self):
        super().__init__("Volcarona", 200, 85, 40, 70, "Bug", "Fire")
        self.moves = {
            "1": Move(
                "Deals fire damage and raises attack", "Volcarona flaps its wings in a fiery dance!", 
                "Fiery Dance", "Fire", "attack", 10, 
                stat_to_fix="attack", effect_value=5, target_self=True
            ),
            "2": Move(
                "Standard bug damage", "Volcarona vibrates its wings rapidly!", 
                "Bug Buzz", "Bug", "attack", 0
            ),
            "3": Move(
                "Increases Attack and Speed", "Volcarona dances gracefully!", 
                "Quiver Dance", "Bug", "attack", 0, 
                is_attack=False, effects=["buff"], # We'll use our list logic here
                stat_to_fix=["attack", "speed"], effect_value=10, target_self=True
            ),
            "4": Move(
                "Massive fire wave with stun chance", "A massive wave of heat crashes down!", 
                "Heat Wave", "Fire", "attack", 20, 
                effects=["stun"]
            )
        }