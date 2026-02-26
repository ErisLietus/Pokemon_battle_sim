def battle(first, second, player,enemy):
            
    if first.is_stunned == 1:
        print(f"{first.name} is stunned cannot move")
        first.is_stunned = 0
        return 0
    else:
        
        if first.is_player_pokemon == True:
            first.choose_move(second)
        else:
            first.random_move(second)

    if second.hp > 0:
         print(f"{second.name} has {second.hp}HP left")
         return 0

    if second.hp <= 0:
        second.hp = 0
        print(f"{second.name} fainted!")
        if second.is_player_pokemon:
            print("GAME OVER!")
            return enemy.name
        else:
            return player.name