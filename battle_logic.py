def attack_target(attacker, target):
        # Determine turn order based on speed
        if attacker.speed >= target.speed:
            first, second = attacker, target
        else:
            first, second = target, attacker
    
        # Battle loop
        while attacker.hp > 0 and target.hp > 0:
            # First attacker's turn
            damage = first.attack - second.defence
            if damage < 1:
                damage = 5
            second.hp -= damage
            print(f"{first.name} attacks {second.name} for {damage} damage!")
        
            if second.hp <= 0:
                second.hp = 0
                print(f"{second.name} fainted!")
                if second.name == attacker.name:
                    print("GAME OVER!")
                    return target.name
                else:
                    attacker.hp = attacker.max_hp
                    return attacker.name
            # Second attacker's turn
            damage = second.attack - first.defence
            if damage < 1:
                damage = 5
            first.hp -= damage
            print(f"{second.name} attacks {first.name} for {damage} damage!")
            
        
            if first.hp <= 0:
                first.hp = 0
                print(f"{first.name} fainted!")
                if first.name == attacker.name:
                    print("GAME OVER!")
                    return target.name
                else:
                    attacker.hp = attacker.max_hp
                    return attacker.name