from battle_contorl import battle_contorl
from pokemon_roster import Pikachu, Charmander, Squirtle, Bulbasaur,Boots, Pokemon
from battle_contorl import win



if win == 1:
    companion = [Pikachu(),Charmander(), Squirtle(), Bulbasaur(), Boots()]
else:  
    companion = [Pikachu(),Charmander(), Squirtle(), Bulbasaur()]    
battle_contorl(companion)