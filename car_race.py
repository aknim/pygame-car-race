import pygame
import sys
import random

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
BLUE = (0, 0, 200)

# Player car
player_width = 50
player_height = 100
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT - player_height - 20
player_speed = 5

# Obstacle cars
obstacle_width = 50
obstacle_height = 100
obstacle_speed = 5
obstacles = []

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

def generate_obstacle():
    x = random.randint(0, SCREEN_WIDTH - obstacle_width)
    y = - obstacle_height # start off-screen
    return [x, y]

def draw_obstacles():
    for obstacle in obstacles:
        pygame.draw.rect(screen, BLUE, (obstacle[0], obstacle[1], obstacle_width, obstacle_height))

def update_obstacles():
    for obstacle in obstacles: 
        obstacle[1] += obstacle_speed

def detect_collision(player_x, player_y):
    for obstacle in obstacles:
        if (
            obstacle[0] - player_width < player_x < obstacle[0] + obstacle_width and
            obstacle[1] - player_height < player_y < obstacle[1] + obstacle_height 

        ):
            return True
    return False

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

    # Generate obstacles randomly
    if random.randint(1, 30) == 1: # Adjust frequency as needed
        obstacles.append(generate_obstacle())
    
    update_obstacles()

    obstacles = [obstacle for obstacle in obstacles if obstacle[1] < SCREEN_HEIGHT]

    # Check for collisions
    if detect_collision(player_x, player_y):
        print("Game Over!")
        running = False

    draw_road()
    draw_player(player_x, player_y)
    draw_obstacles()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()