from base_pokemon import Pokemon
from pokemon_roster import Pikachu, Charmander, Squirtle,Bulbasaur, Boots
from battle_logic import attack_target
import random


def battle_contorl(companions, player_pokemon=None, battle_count=0):
    
    if player_pokemon is None:
        print("Available Pokemon:")
        for c in companions:
            print(f" - {c.name}")

        print("Press Enter for random Pokemon")
        choice = input("Choose your Pokemon: ")
        
        # Look for the object that matches the name
        selected = None
        for c in companions:
            if c.name.lower() == choice.lower():
                selected = c
                break
            
        if choice == "":
            print("Choosing a random companion...")
            selected = random.choice(companions)
        elif selected is None:
            print(f"I couldn't find a Pokemon named '{choice}'. Picking a random one for you.")
            selected = random.choice(companions)
            
        player_pokemon = selected
        companions.remove(player_pokemon)
        player_pokemon.is_player_pokemon = True
    
    # Check if the gauntlet is over
    if not companions or battle_count == 5:
        print(f"CONGRATULATIONS! {player_pokemon.name} Wins the game!")
        return
    
    # Pick a random enemy from the remaining list
    enemy_pokemon = random.choice(companions)
    companions.remove(enemy_pokemon)

    print(f"\nBATTLE {battle_count + 1}: {player_pokemon.name} vs {enemy_pokemon.name}")
    
    winner = player_pokemon.start_battle(enemy_pokemon)

    if winner == player_pokemon.name:
        battle_count += 1
    
        # Nurse Joy's healing magic!
        player_pokemon.hp = player_pokemon.max_hp
        player_pokemon.attack = player_pokemon.max_attack
        player_pokemon.defence = player_pokemon.max_defence
        player_pokemon.speed = player_pokemon.max_speed
        player_pokemon.is_stunned = False
        player_pokemon.has_turn = True
    
        print(f"\nNurse Joy: 'Your {player_pokemon.name} is all healed up! Good luck in the next round!'")
        return battle_contorl(companions, player_pokemon, battle_count)
    else:
        print(f"{player_pokemon.name} was defeated. Better luck next time!")

