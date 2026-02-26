from Pokemon import Pikachu, Charmander, Squirtle, Bulbasaur, Pokemon
from battle_logic import attack_target
import random


def battle(companion, player_pokemon=None):
    
    if player_pokemon is None:
        player_class = random.choice(companion)
        companion.remove(player_class)
        player_pokemon = player_class()
    
    if companion == []:
        return print(f"{player_pokemon.name} Wins the game!")
    
    enemy_class = random.choice(companion)
    companion.remove(enemy_class)
    enemy_pokemon = enemy_class()

    print(f"{player_pokemon.name} vs {enemy_pokemon.name}")
    
    winner = player_pokemon.start_battle(enemy_pokemon)
    print(f"DEBUG: winner = {winner}, player = {player_pokemon.name}")

    if winner == player_pokemon.name:
        return battle(companion, player_pokemon)
    else:
        print(f"{player_pokemon.name} was defeated. Better luck next time!")

