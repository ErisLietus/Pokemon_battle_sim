class BattleController:
    def handle_player_turn(self, player, enemy):
        # The UI logic stays here
        self.display_moves(player.moves)
        choice = self.get_user_input() 
        move = player.moves[choice]
        move.execute(player, enemy)