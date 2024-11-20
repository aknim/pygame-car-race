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
RED = (200, 0, 0)

# Player car
player_width = 50
player_height = 100
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT - player_height - 20
player_speed = 5

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
        
def draw_player(x, y):
    pygame.draw.rect(screen, RED, (x, y, player_width, player_height))
# Game loop
running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
        player_x += player_speed

    draw_road()
    draw_player(player_x, player_y)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()