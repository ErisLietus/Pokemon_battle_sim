import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants for our window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Create the window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pokemon Battle Academy: Pygame Edition")
clock = pygame.time.Clock()

def draw_hp_bar(x, y, current_hp, max_hp):
    # Calculate width based on percentage
    ratio = current_hp / max_hp
    pygame.draw.rect(screen, RED, (x, y, 200, 20)) # Red background
    pygame.draw.rect(screen, GREEN, (x, y, 200 * ratio, 20)) # Green health

def main_game_loop():
    # Let's pretend we have a Pikachu for testing
    # In the future, we will pass your actual Pokemon objects here!
    
    running = True
    while running:
        # 1. Event Handling (Input)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        # 2. Update Logic (We'll put battle math here later)

        # 3. Drawing (The "Render" phase)
        screen.fill(WHITE) # Clear screen with white
        
        # Draw a temporary "Pokemon" (a rectangle for now)
        pygame.draw.rect(screen, (255, 220, 0), (100, 300, 150, 150)) # Player
        pygame.draw.rect(screen, (100, 100, 100), (550, 100, 150, 150)) # Enemy
        
        # Draw HP Bars
        draw_hp_bar(100, 270, 90, 90) # Player HP
        draw_hp_bar(550, 70, 150, 150) # Enemy HP

        # Refresh the screen
        pygame.display.flip()
        
        # Maintain 60 FPS
        clock.tick(FPS)

if __name__ == "__main__":
    main_game_loop()