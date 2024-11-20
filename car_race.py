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
GREEN = (0, 255, 0)

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

# Score and difficulty
score = 0
difficulty_increase_rate = 1
difficulty_level = 1

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
    global score
    for obstacle in obstacles: 
        obstacle[1] += obstacle_speed
        if obstacle[1] > SCREEN_HEIGHT:
            obstacles.remove(obstacle)
            score += 1

def detect_collision(player_x, player_y):
    for obstacle in obstacles:
        if (
            obstacle[0] - player_width < player_x < obstacle[0] + obstacle_width and
            obstacle[1] - player_height < player_y < obstacle[1] + obstacle_height 

        ):
            return True
    return False

def display_score():
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, GREEN)
    screen.blit(score_text, (10, 10))

def display_text(text, font_size, color, y_offset=0):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + y_offset))
    screen.blit(text_surface, text_rect)

def start_screen():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                running = False
        
        screen.fill(GRAY)
        display_text("Car Racing Game", 48, WHITE, -50)
        display_text("Press Enter to Start", 36, WHITE, 50)
        pygame.display.flip()
        clock.tick(FPS)

def game_over_screen():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                restart_game()

        screen.fill(GRAY)
        display_text("Game Over", 48, RED, -50)
        display_text(f"Final Score: {score}", 36, WHITE, 0)
        display_text("Press Enter to Restart", 36, WHITE, 50)
        pygame.display.flip()
        clock.tick(FPS)

def restart_game():
    global score, obstacles, player_x
    score = 0
    obstacles = []
    player_x = SCREEN_WIDTH // 2 - player_width // 2
    main_game()

# Main Game loop
def main_game():
    global player_x, player_y, score, obstacles, obstacle_speed, difficulty_level
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

        # Check for collisions
        if detect_collision(player_x, player_y):
            game_over_screen()

        # Increase difficulty based on score
        if score // difficulty_increase_rate > difficulty_level:
            obstacle_speed += 1
            difficulty_level += 1

        draw_road()
        draw_player(player_x, player_y)
        draw_obstacles()
        display_score()

        pygame.display.flip()
        clock.tick(FPS)

# Start the game
start_screen()
main_game()