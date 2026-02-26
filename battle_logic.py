def attack_target(attacker, target):
        # Determine turn order based on speed
        if attacker.speed >= target.speed:
            first, second = attacker, target
        else:
            first, second = target, attacker
    
        # Battle loop
        while attacker.hp > 0 and target.hp > 0:
            # First attacker's turn
            if first.is_stunned:
                    print(f"{first.name} is stunned cannot move")
            else:
                if first.is_player_pokemon == True:
                    first.choose_move(second)
                else:
                    first.random_move(second)
            if second.hp > 0:
                 print(f"{second.name} has {second.hp}HP left")

            if second.hp <= 0:
                second.hp = 0
                print(f"{second.name} fainted!")
                if second.name == attacker.name:
                    print("GAME OVER!")
                    return target.name
                else:
                    attacker.hp = attacker.max_hp
                    attacker.attack = attacker.max_attack
                    attacker.defence = attacker.max_defence
                    attacker.speed = attacker.max_speed
                    attacker.is_stunned = False
                    return attacker.name
            # Second attacker's turn
            if second.is_stunned:
                    print(f"{second.name} is stunned cannot move")
            else:
                if second.is_player_pokemon == True:
                    second.choose_move(first)
                else:
                    second.random_move(first)

            if first.hp > 0:
                 print(f"{first.name} has {first.hp}HP left")

            if first.hp <= 0:
                first.hp = 0
                print(f"{first.name} fainted!")
                if first.name == attacker.name:
                    print("GAME OVER!")
                    return target.name
                else:
                    attacker.hp = attacker.max_hp
                    attacker.hp = attacker.max_hp
                    attacker.attack = attacker.max_attack
                    attacker.defence = attacker.max_defence
                    attacker.speed = attacker.max_speed
                    attacker.is_stunned = False
                    return attacker.name