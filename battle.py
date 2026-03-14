def battle(first, second, player, enemy):
    if first.is_stunned == 1:
        print(f"{first.name} is stunned cannot move")
        first.is_stunned = 0
        return 0
    
    # Perform the move
    if first.is_player_pokemon:
        first.choose_move(second)
    else:
        first.random_move(second)

    # 1. Check if the ATTACKER fainted from recoil
    if first.hp <= 0:
        first.hp = 0
        print(f"{first.name} fainted from recoil!")
        return enemy.name if first.is_player_pokemon else player.name

    # 2. Check if the TARGET fainted from the attack
    if second.hp <= 0:
        second.hp = 0
        print(f"{second.name} fainted!")
        return player.name if first.is_player_pokemon else enemy.name

    # 3. If both are still standing
    print(f"{second.name} has {second.hp}HP left")
    return 0