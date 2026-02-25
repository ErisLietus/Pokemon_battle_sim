class Pokemon: 
    def __init__(self, name, pokemon_type,hp,attack,defence,speed):
        self.name = name 
        self.type = pokemon_type
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defence = defence
        self.speed = speed
    

class Pikachu(Pokemon):
    def __init__(self):
        super().__init__("Pikachu", "Electric", 100, 39, 25, 51)

class Charmander(Pokemon):
    def __init__(self):
        super().__init__("Charmander", "Fire", 100, 51, 25, 25)

class Squirtle(Pokemon):
    def __init__(self):
        super().__init__("Squirtle", "Water", 100, 39, 51, 20)

class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__("Bulbasaur", "Grass", 100, 51, 30, 10)