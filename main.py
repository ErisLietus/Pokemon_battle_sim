import battle_contorl
from pokemon_roster import Pikachu, Charmander, Squirtle, Bulbasaur, Eevee, Snorlax, Boots
from advanced_pokemon import Gardevoir, Stakataka, Vanilluxe, Milotic, Volcarona, Dragonite
import random

def main():
    print("Welcome to the Pokemon Battle Academy!")
    
    while True:
        # Refresh the leagues every time the loop starts
        starter_league = [Pikachu(), Charmander(), Squirtle(), Bulbasaur(), Eevee(), Snorlax()]
        starter_league_2 = [Pikachu(), Charmander(), Squirtle(), Bulbasaur(), Eevee(), Snorlax(), Boots()]
        advanced_league = [Gardevoir(), Stakataka(), Vanilluxe(), Milotic(), Volcarona(), Dragonite()]
        
        # Check the win status from the module
        if battle_contorl.win == 1:
            print("\n--- Advanced League Unlocked! ---")
            choice = input("Choose 'starter', 'advanced', or press Enter for random: ").lower().strip()
            
            if choice == "starter":
                companion = starter_league_2
            elif choice == "advanced":
                companion = advanced_league
            else:
                companion = random.choice([starter_league, advanced_league])
        else:
            companion = starter_league
            
        # Call the function specifically from the module
        battle_contorl.battle_contorl(companion)
        
        # Ask to play again so the script doesn't just end
        again = input("\nWould you like to play another gauntlet? (y/n): ").lower().strip()
        if again != 'y':
            break

    print("\nYour journey ends here. Safe travels, apprentice!")

if __name__ == "__main__":
    main()