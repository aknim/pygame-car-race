import pygame
import sys

pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
YELLOW = (255, 255, 0)

# Setup screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Car Racing Game")

# Clock for controlling frame rate
clock = pygame.time.Clock()

def draw_road():
    screen.fill(GRAY)

    # Draw lanes
    lane_width = SCREEN_WIDTH // 5
    for i in range(1, 5):
        pygame.draw.line(screen, WHITE, 
                         (lane_width * i, 0), 
                         (lane_width * i, SCREEN_HEIGHT), 2)
        
    # Add lane markings in the center
    for y in range(0, SCREEN_HEIGHT, 40):
        pygame.draw.line(screen, YELLOW, (SCREEN_WIDTH // 2 - 5, y),
                        (SCREEN_WIDTH // 2 + 5, y + 20), 3)
        
# Game loop
running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_road()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()