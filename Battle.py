from Pokemon import Pikachu, Charmander, Squirtle, Bulbasaur, Pokemon
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
    
    winner = player_pokemon.attack_target(enemy_pokemon)
    
    if winner == player_pokemon.name:
        battle(companion, player_pokemon)
    else:
        print(f"{player_pokemon.name} was defeated. Better luck next time!")


