from base_pokemon import Pokemon
from move import Move

class Pikachu(Pokemon):
    def __init__(self):
        super().__init__("Pikachu", 90, 40, 15, 50, "Electric")
        self.moves = {
            "1": Move(
                "Increases Pikachu's speed", "Pikachu dashed around the arena!", 
                "Dash", "Normal", "speed", 5, 
                is_attack=False, stat_to_fix=["speed"], effect_value=5, target_self=True
            ),
            "2": Move(
                "Hits based on speed", "Pikachu lunges with a Quick Attack!", 
                "Quick Attack", "Normal", "speed", 0
            ),
            "3": Move(
                "Hard hit with stun chance", "Lightning crackles on Pikachu's tail!", 
                "Lightning Tail", "Electric", "attack", 10, 
                effects=["stun"]
            ),
            "4": Move(
                "Lowers opponent's defense", "Pikachu wags its tail tauntingly.", 
                "Tail Whip", "Normal", "attack", 0, 
                is_attack=False, stat_to_fix=["defence"], effect_value=-5, target_self=False
            )
        }

class Charmander(Pokemon):
    def __init__(self):
        super().__init__("Charmander", 100, 35, 20, 35, "Fire")
        self.moves = {
            "1": Move(
                "Standard fire damage", "Charmander lets out a small flame!", 
                "Ember", "Fire", "attack", 0
            ),
            "2": Move(
                "High damage with recoil", "Charmander breathes wild fire!", 
                "Dragon Rage", "Dragon", "attack", 15, 
                effects=["recoil"], effect_value=15
            ),
            "3": Move(
                "Increases attack", "Charmander cheered itself on!", 
                "Cheer", "Normal", "attack", 0, 
                is_attack=False, stat_to_fix=["attack"], effect_value=5, target_self=True
            ),
            "4": Move(
                "Lowers opponent's speed", "Charmander makes a scary face!", 
                "Scary Face", "Normal", "attack", 0, 
                is_attack=False, stat_to_fix=["speed"], effect_value=-5, target_self=False
            )
        }

class Squirtle(Pokemon):
    def __init__(self):
        super().__init__("Squirtle", 120, 25, 35, 20, "Water")
        self.moves = {
            "1": Move(
                "Standard water damage", "Squirtle shoots a jet of water!", 
                "Water Gun", "Water", "attack", 0
            ),
            "2": Move(
                "Raises defense", "Squirtle withdraws into its shell.", 
                "Withdraw", "Normal", "attack", 0, 
                is_attack=False, stat_to_fix=["defence"], effect_value=5, target_self=True
            ),
            "3": Move(
                "Protects for one turn", "Squirtle hides inside its shell!", 
                "Protect", "Normal", "attack", 0, 
                is_attack=False, effects=["shield"]
            ),
            "4": Move(
                "Damage based on defense", "Squirtle slams its shell into the target!", 
                "Skull Bash", "Normal", "defence", 0
            )
        }

class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__("Bulbasaur", 110, 40, 25, 15, "Grass", "Poison")
        self.moves = {
            "1": Move(
                "Standard grass damage", "Bulbasaur whips its vines!", 
                "Vine Whip", "Grass", "attack", 0
            ),
            "2": Move(
                "Heals 30 HP", "Bulbasaur absorbs sunlight!", 
                "Synthesis", "Grass", "attack", 0, 
                is_attack=False, effects=["heal"], effect_value=30
            ),
            "3": Move(
                "High critical hit chance", "Bulbasaur launches sharp leaves!", 
                "Razor Leaf", "Grass", "attack", -10, 
                effects=["increased crit"]
            ),
            "4": Move(
                "Lowers opponent's attack", "Bulbasaur growls scarying the opponent!", 
                "Growl", "Normal", "attack", 0, 
                is_attack=False, stat_to_fix=["attack"], effect_value=-5, target_self=False
            )
        }

class Eevee(Pokemon):
    def __init__(self):
        super().__init__("Eevee", 110, 40, 20, 25, "Normal")
        self.moves = {
            "1": Move(
                "Standard dark damage", "Eevee bites the opponent!", 
                "Bite", "Dark", "attack", 0
            ),
            "2": Move(
                "Hits through protection", "Eevee's voice rings out!", 
                "Disarming Voice", "Fairy", "attack", -5, 
                effects=["shield_breaker"]
            ),
            "3": Move(
                "Hits 3 times", "Eevee unleashes a flurry of stars!", 
                "Swift", "Normal", "attack", -10, 
                hits=3
            ),
            "4": Move(
                "Lowers opponent's attack", "Eevee looks adorable!", 
                "Charm", "Normal", "attack", 0, 
                is_attack=False, stat_to_fix=["attack"], effect_value=-5, target_self=False
            )
        }

class Snorlax(Pokemon):
    def __init__(self):
        super().__init__("Snorlax", 160, 50, 40, 5, "Normal")
        self.moves = {
            "1": Move(
                "Heavy normal damage", "Snorlax slams its massive body!", 
                "Body Slam", "Normal", "attack", 10
            ),
            "2": Move(
                "Heals 50 HP but stuns user", "Snorlax takes a quick nap!", 
                "Rest", "Normal", "attack", 0, 
                is_attack=False, effects=["heal", "stun"], effect_value=50, target_self=True
            ),
            "3": Move(
                "Lowers opponent's speed", "Snorlax lets out a massive yawn!", 
                "Yawn", "Normal", "attack", 0, 
                is_attack=False, stat_to_fix=["speed"], effect_value=-10, target_self=False
            ),
            "4": Move(
                "Increases own defense", "Snorlax forgets its troubles.", 
                "Amnesia", "Normal", "attack", 0, 
                is_attack=False, stat_to_fix=["defence"], effect_value=10, target_self=True
            )
        }

class Boots(Pokemon):
    def __init__(self):
        super().__init__("Boots", 150, 40, 30, 30, "Psychic", "Ice")
        self.moves = {
            "1": Move(
                "Psychic blast", "Boots shares enchanted wisdom!", 
                "Enchanted Wisdom", "Psychic", "attack", 0
            ),
            "2": Move(
                "Icy shards based on speed", "Boots creates crystal shards!", 
                "Crystal Clarity", "Ice", "speed", 10
            ),
            "3": Move(
                "Lowers enemy defense", "Boots finds a bug in the code!", 
                "Debug", "Normal", "attack", 0, 
                is_attack=False, stat_to_fix=["defence"], effect_value=-10, target_self=False
            ),
            "4": Move(
                "Massive damage but stuns user", "Boots drops the temperature to absolute zero!", 
                "Deep Freeze", "Ice", "attack", 40, 
                effects=["stun"], target_self=True
            )
        }
    