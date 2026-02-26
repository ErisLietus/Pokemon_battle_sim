from base_pokemon import Pokemon

class Pikachu(Pokemon):
    def __init__(self):
        super().__init__("Pikachu", "Electric", 90, 40, 15, 50)
        self.moves = {
            "1": ("Thunder Shock", self.thunder_shock),
            "2": ("Quick Attack", self.quick_attack),
            "3": ("Lighting Tail", self.lighting_tail),
            "4": ("Tail Whip", self.tail_whip)
        }
    
    def thunder_shock(self, target):
       
        self.perform_attack(target, self.attack, "Thunder Shock", "Electric")
        

    def quick_attack(self, target):
        self.perform_attack(target, self.speed, "Quick Attack", "Normal")
        

    def lighting_tail(self, target):
        self.perform_attack(target, self.attack + self.speed, "Lighting Tail")
        self.is_stunned = True
        print(f"{self.name} is stunned!")
    
    def tail_whip(self, target):
        target.defence -= 10
        if target.defence < 0:
            target.defence = 0
        print(f"{self.name} used Tail Whip, lowers {target.name}'s defence!")
        print(f"{target.name} has {target.defence} left")
        

class Charmander(Pokemon):
    def __init__(self):
        super().__init__("Charmander", "Fire", 100, 35, 20, 35)
        self.moves = {
            "1": ("Thunder Shock", self.thunder_shock),
            "2": ("Quick Attack", self.quick_attack),
            "3": ("Lighting Tail", self.lighting_tail),
            "4": ("Tail Whip", self.tail_whip)
        }
    
    def thunder_shock(self, target):
       
        self.perform_attack(target, self.attack, "Thunder Shock", "Electric")
        

    def quick_attack(self, target):
        self.perform_attack(target, self.speed, "Quick Attack", "Normal")
        

    def lighting_tail(self, target):
        self.perform_attack(target, self.attack + self.speed, "Lighting Tail", "Electric")
        self.is_stunned = True
        print(f"{self.name} is stunned!")
    
    def tail_whip(self, target):
        target.defence -= 10
        if target.defence < 0:
            target.defence = 0
        print(f"{self.name} used Tail Whip, lowers {target.name}'s defence!")
        print(f"{target.name} has {target.defence} left")

class Squirtle(Pokemon):
    def __init__(self):
        super().__init__("Squirtle", "Water", 120, 25, 35, 20)
        self.moves = {
            "1": ("Thunder Shock", self.thunder_shock),
            "2": ("Quick Attack", self.quick_attack),
            "3": ("Lighting Tail", self.lighting_tail),
            "4": ("Tail Whip", self.tail_whip)
        }
    
    def thunder_shock(self, target):
       
        self.perform_attack(target, self.attack, "Thunder Shock", "Electric")
        

    def quick_attack(self, target):
        self.perform_attack(target, self.speed, "Quick Attack", "Normal")
        

    def lighting_tail(self, target):
        self.perform_attack(target, self.attack + self.speed, "Lighting Tail","Electric")
        self.is_stunned = True
        print(f"{self.name} is stunned!")
    
    def tail_whip(self, target):
        target.defence -= 10
        if target.defence < 0:
            target.defence = 0
        print(f"{self.name} used Tail Whip, lowers {target.name}'s defence!")
        print(f"{target.name} has {target.defence} left")
class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__("Bulbasaur", "Grass", 110, 40, 25, 15)
        self.moves = {
            "1": ("Thunder Shock", self.thunder_shock),
            "2": ("Quick Attack", self.quick_attack),
            "3": ("Lighting Tail", self.lighting_tail),
            "4": ("Tail Whip", self.tail_whip)
        }
    
    def thunder_shock(self, target):
       
        self.perform_attack(target, self.attack, "Thunder Shock", "Electric")
        

    def quick_attack(self, target):
        self.perform_attack(target, self.speed, "Quick Attack", "Normal")
        

    def lighting_tail(self, target):
        self.perform_attack(target, self.attack + self.speed, "Lighting Tail", "Electric")
        self.is_stunned = True
        print(f"{self.name} is stunned!")
    
    def tail_whip(self, target):
        target.defence -= 10
        if target.defence < 0:
            target.defence = 0
        print(f"{self.name} used Tail Whip, lowers {target.name}'s defence!")
        print(f"{target.name} has {target.defence} left")

class Boots(Pokemon):
    def __init__(self):
        super().__init__("Boots", "Psychic", 150, 45, 30, 30)
        self.moves = {
            "1": ("Thunder Shock", self.thunder_shock),
            "2": ("Quick Attack", self.quick_attack),
            "3": ("Lighting Tail", self.lighting_tail),
            "4": ("Tail Whip", self.tail_whip)
        }
    
    def thunder_shock(self, target):
        damage = self.attack - target.defence
        if damage < 0:
            damage = 5
        target.hp -= damage
        print(f"{self.name} uses Thunder Shock for {damage} damage!")
        

    def quick_attack(self, target):
        damage = self.speed - target.defence
        target.hp -= damage
        if damage < 0:
            damage = 5
        print(f"{self.name} uses Quick Attack for {damage} damage!")
        

    def lighting_tail(self,target):
        damage = self.attack + self.speed - target.defence
        target.hp -= damage
        if damage < 0:
            damage = 5
        self.is_stunned = True
        print(f"{self.name} uses Lighting Tail for {damage} damage!")
        print(f"{self.name} is stunned!")
    
    def tail_whip(self, target):
        target.defence -= 10
        if target.defence < 0:
            target.defence = 0
        print(f"{self.name} used Tail Whip, lowers {target.name}'s defence!")