from battle import battle

def attack_target(player, target):
        # Determine turn order based on speed
        if player.speed >= target.speed:
            first, second = player, target
        else:
            first, second = target, player
    
        

        if first.has_turn:
            result = battle(first, second, player, target)
            if result == 0:
                first.has_turn = False 
                return attack_target(player, target)
            else:
                return result
        else:
            result = battle(second, first, player, target)
            first.has_turn = True
            if result == 0:
                return attack_target(player, target)
            else:
                return result
         