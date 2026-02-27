from battle import battle

def attack_target(player, target):
    # Determine turn order once at the start
    if player.speed >= target.speed:
        first, second = player, target
    else:
        first, second = target, player

    # Keep looping as long as both are standing
    while player.hp > 0 and target.hp > 0:
        if first.has_turn:
            result = battle(first, second, player, target)
            first.has_turn = False # Switch turn state
        else:
            result = battle(second, first, player, target)
            first.has_turn = True # Switch turn state

        # If battle() returned a name (the winner), return it to end the function
        if result != 0:
            return result
         