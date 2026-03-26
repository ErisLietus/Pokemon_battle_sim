import pygame
import sys
from advanced_pokemon import Gardevoir, Dragonite
from move import Move

# 1. Setup
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pokemon Battle GUI")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

# 2. Initialize our actual Pokemon objects!
player = Gardevoir()
enemy = Dragonite()

def draw_pokemon_info(pkmn, x, y, is_player):
    # Draw Name
    name_text = font.render(f"{pkmn.name} (Lvl 50)", True, (0, 0, 0))
    screen.blit(name_text, (x, y))
    
    # Draw HP Bar Background (Gray)
    pygame.draw.rect(screen, (200, 200, 200), (x, y + 30, 200, 15))
    
    # Calculate HP Width
    current_hp = max(0, pkmn.hp)
    hp_ratio = current_hp / pkmn.max_hp
    bar_color = (0, 255, 0) if hp_ratio > 0.5 else (255, 165, 0) if hp_ratio > 0.2 else (255, 0, 0)
    
    # Draw Current HP (Green/Yellow/Red)
    pygame.draw.rect(screen, bar_color, (x, y + 30, 200 * hp_ratio, 15))
    
    # Draw HP Numbers
    hp_text = font.render(f"{pkmn.hp}/{pkmn.max_hp}", True, (0, 0, 0))
    screen.blit(hp_text, (x, y + 50))

def draw_buttons(pokemon):
    # We will draw 4 buttons in a 2x2 grid at the bottom
        button_font = pygame.font.SysFont("Arial", 18)
        mouse_pos = pygame.mouse.get_pos()
    
    # We'll store the button rectangles so we can check for clicks later
        button_rects = {}
    
        x_start, y_start = 450, 400
        width, height = 150, 45
        padding = 10

        for i, (key, move) in enumerate(pokemon.moves.items()):
            # Calculate grid position (0,1 top row; 2,3 bottom row)
            col = i % 2
            row = i // 2
            rect = pygame.Rect(x_start + (width + padding) * col, 
                           y_start + (height + padding) * row, 
                           width, height)
        
        # Hover effect: Change color if mouse is over the button
            color = (180, 180, 180) if rect.collidepoint(mouse_pos) else (220, 220, 220)
        
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, (0, 0, 0), rect, 2) # Border
        
        # Draw Move Name
            text = button_font.render(move.name, True, (0, 0, 0))
            text_rect = text.get_rect(center=rect.center)
            screen.blit(text, text_rect)
        
            button_rects[key] = rect
        
        return button_rects

# 3. Main Loop
while True:
    button_rects = draw_buttons(player) # Draw them and get their positions

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # Left click
                for move_key, rect in button_rects.items():
                    if rect.collidepoint(event.pos):
                        # ACTION! Execute the move
                        move = player.moves[move_key]
                        damage_dealt = move.execute(player, enemy)
                        print(f"GUI: {player.name} dealt {damage_dealt} damage!")

    screen.fill((255, 255, 255)) # White background

    # Draw our "Stage"
    # Enemy is usually top-right, Player is bottom-left
    draw_pokemon_info(enemy, 500, 50, False)
    draw_pokemon_info(player, 100, 400, True)
    draw_buttons(player)

    pygame.display.flip()
    clock.tick(60)