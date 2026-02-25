class Pokemon: 
    def __init__(self, name, pokemon_type,hp,attack,defence,speed):
        self.name = name 
        self.type = pokemon_type
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defence = defence
        self.speed = speed
        
    
    
    def attack_target(self, target):
        # Determine turn order based on speed
        if self.speed >= target.speed:
            first, second = self, target
        else:
            first, second = target, self
    
        # Battle loop
        while self.hp > 0 and target.hp > 0:
            # First attacker's turn
            damage = first.attack - second.defence
            if damage < 1:
                damage = 5
            second.hp -= damage
            print(f"{first.name} attacks {second.name} for {damage} damage!")
        
            if second.hp <= 0:
                second.hp = 0
                print(f"{second.name} fainted!")
                if second.name == self.name:
                    print("GAME OVER!")
                    return target.name
                else:
                    self.hp = self.max_hp
                    return self.name
            # Second attacker's turn
            damage = second.attack - first.defence
            if damage < 1:
                damage = 5
            first.hp -= damage
            print(f"{second.name} attacks {first.name} for {damage} damage!")
            
        
            if first.hp <= 0:
                first.hp = 0
                print(f"{first.name} fainted!")
                if first.name == self.name:
                    print("GAME OVER!")
                    return target.name
                else:
                    self.hp = self.max_hp
                    return self.name
        
    

class Pikachu(Pokemon):
    def __init__(self):
        super().__init__("Pikachu", "Electric", 90, 40, 15, 50)

    def electric_tail(self, target):
        damage = self.attack + self.speed - target.defence
        target.hp -= damage
        print(f"{self.name} uses Electric Tail on {target.name} for {damage} damage!")

class Charmander(Pokemon):
    def __init__(self):
        super().__init__("Charmander", "Fire", 100, 35, 20, 35)

class Squirtle(Pokemon):
    def __init__(self):
        super().__init__("Squirtle", "Water", 120, 25, 35, 20)

class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__("Bulbasaur", "Grass", 110, 40, 25, 15)

class Boots(Pokemon):
    def __init__(self):
        super().__init__("Boots", "Psychic", 150, 45, 30, 30)

