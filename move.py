import random 

class Move:
    def __init__(self, description,favour_text, name, move_type, attack_stat_name, power,
                    is_attack = True, 
                    effects =None,
                    effect_value=0,
                    stat_to_fix=None,
                    hits=1,
                    target_self=False
                    ):
        self.description = description
        self.favour_text = favour_text
        self.name = name
        self.type = move_type
        self.attack_stat_name = attack_stat_name # "attack", "defence", or "speed"
        self.power = power
        self.is_attack = is_attack
        self.effects = effects if effects is not None else []
        self.effect_value = effect_value
        self.stat_to_fix = stat_to_fix if stat_to_fix is not None else []
        self.hits = hits
        self.target_self = target_self

    def execute(self, user, target):
        print(f"{user.name} used {self.name}")
        print(self.favour_text)
        # 1. Pre-attack setup
        if  "never misses" in self.effects:
            self._never_misses(user)
        elif "shield_breaker" in self.effects:
            target.is_protected = 0
            print(f"{self.name} shattered the shield!")
        
        # 2. Dynamic Stat Lookup
        # This gets user.attack, user.defence, or user.speed based on the move!
        base_stat = getattr(user, self.attack_stat_name)
        total_power = base_stat + self.power

        # 3. Critical Hit Logic
        if "increased crit" in self.effects and random.randint(1, 3) == 3:
            total_power *= 1.5
            print("A massive critical hit!")
        elif random.randint(1, 10) == 10: # Standard 10% crit chance for all
            total_power *= 1.5
            print("A Critical Hit!")
        
        # 4. Perform the Attack(s)
        damage = 0 
        # Only attack if power > 0 or it's a "never miss" move
        if self.is_attack == True:
            for _ in range(self.hits):
                damage += user.perform_attack(target, total_power, self.name, self.type)
        
        # 5. Cleanup and Effects
        user.cannot_miss = 0
        
        # This handles Buffs AND Debuffs in one go!
        if self.stat_to_fix != None:
            for stat in self.stat_to_fix:
                destination = user if self.target_self else target
                destination.modify_stat(self.stat_to_fix, self.effect_value)

        for effect in self.effects:
            
            
            for effect in self.effects:

                if effect == "heal":
                    self._apply_heal(user, self.effect_value)

                if effect == "stun":
                    destination = user if self.target_self else target
        
                    if self.target_self:
                        destination.is_stunned = 1
            
                    else:
                        self._apply_stun(destination)
            
            if effect == "recoil":
                self._recoil(user, self.effect_value)
            
            if effect == "shield_breaker":
                target.is_protected = 0

    def _apply_heal(self, user, amount):
        user.hp = min(user.hp + amount, user.max_hp)
        print(f"{user.name} healed for {amount}!")

    def _apply_stun(self, target):
        if random.randint(1, 4) == 4:
            target.is_stunned = 1
            print(f"{target.name} is stunned!")

    def _recoil(self, user, amount):
        user.hp = max(0, user.hp - amount)
        print(f"{user.name} recoiled and took {amount} damage!")

    def _never_misses(self, user): 
        user.cannot_miss = 1
