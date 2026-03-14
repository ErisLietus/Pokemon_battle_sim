from base_pokemon import Pokemon
from pokemon_roster import Pikachu, Charmander, Squirtle,Bulbasaur, Boots
from battle_logic import attack_target
import random
import sys
from main import main
win = 0

def battle_control(companions, player_pokemon=None, battle_count=0):
    if player_pokemon is None:
        selected = None
        
        # Start a loop that only breaks when a Pokemon is successfully chosen
        while selected is None:
            print("\nAvailable Pokemon:")
            for c in companions:
                print(f" - {c.name}")

            print("Press Enter for random Pokemon")
            choice = input("Choose your Pokemon: ").lower().strip()
            
            # Handle the random choice first
            if choice == "":
                print("Choosing a random companion...")
                selected = random.choice(companions)
                break # Exit the while loop
            
            # Look for the object that matches the name
            for c in companions:
                if c.name.lower() == choice:
                    selected = c
                    break
            
            # If after checking all companions, selected is still None
            if selected is None:
                print(f"\n[!] I couldn't find a Pokemon named '{choice}'. Please try again!")
            
        player_pokemon = selected
        companions.remove(player_pokemon)
        player_pokemon.is_player_pokemon = True
    
    # Check if the gauntlet is over
    if not companions or battle_count == 3:
        print(f"CONGRATULATIONS! {player_pokemon.name} Wins the game!")
        
        global win
        if win == 0:
            print(f"\n\nHang on a Second. A new challanger appears the final boss Boots!!")
            enemy_pokemon = Boots()
            winner = player_pokemon.start_battle(enemy_pokemon)
            if winner == enemy_pokemon.name:
               print(f"{player_pokemon.name} was defeated. Better luck next time!")
               
               sys.exit()  
        win = 1
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
        player_pokemon.is_stunned = 0
        player_pokemon.has_turn = True
        player_pokemon.is_guarded = 0

        print(f"\nNurse Joy: 'Your {player_pokemon.name} is all healed up! Good luck in the next round!'")
        return battle_control(companions, player_pokemon, battle_count)
    else:
        print(f"{player_pokemon.name} was defeated. Better luck next time!")
        again = input("\nWould you like to play another gauntlet? (y/n): ").lower().strip()
        if again != 'y':
            print("\nYour journey ends here. Safe travels, apprentice!")
            sys.exit()
        else:
            main()

