import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50, 150)  # Semi-transparent gray

# Fonts
FONT = pygame.font.Font(None, 36)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Person Parkour Game")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Game states
MENU = "menu"
PLAYING = "playing"
current_state = MENU

# Mission objectives
objectives = ["Reach the first platform", "Find the key", "Get to the exit"]
current_objective_index = 0

# Player settings
player_pos = [400, 300]  # Initial player position
player_speed = 5

# Platforms
platforms = [
    pygame.Rect(300, 500, 200, 20),
    pygame.Rect(550, 400, 200, 20),
    pygame.Rect(200, 300, 200, 20),
    pygame.Rect(450, 200, 200, 20),
]

def draw_menu():
    screen.fill(BLACK)
    title_text = FONT.render("Parkour Game", True, WHITE)
    start_text = FONT.render("Press ENTER to Start", True, WHITE)
    exit_text = FONT.render("Press ESC to Exit", True, WHITE)

    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 200))
    screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, 300))
    screen.blit(exit_text, (WIDTH // 2 - exit_text.get_width() // 2, 350))

def draw_game():
    screen.fill(BLACK)

    # Draw platforms
    for platform in platforms:
        pygame.draw.rect(screen, WHITE, platform)

    # Draw player
    pygame.draw.circle(screen, (0, 255, 0), player_pos, 10)

    # Draw objectives menu
    objectives_surf = pygame.Surface((300, 100), pygame.SRCALPHA)
    objectives_surf.fill(GRAY)
    screen.blit(objectives_surf, (10, 10))

    y_offset = 15
    for i, obj in enumerate(objectives):
        color = (255, 255, 255) if i == current_objective_index else (180, 180, 180)
        obj_text = FONT.render(obj, True, color)
        screen.blit(obj_text, (20, 10 + y_offset))
        y_offset += 30

def handle_menu_events():
    global current_state
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                current_state = PLAYING
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

def handle_game_events():
    global current_objective_index
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()

    # Move player
    if keys[pygame.K_w]:
        player_pos[1] -= player_speed
    if keys[pygame.K_s]:
        player_pos[1] += player_speed
    if keys[pygame.K_a]:
        player_pos[0] -= player_speed
    if keys[pygame.K_d]:
        player_pos[0] += player_speed

    # Check if player reaches the next platform for the objective
    if platforms[current_objective_index].collidepoint(player_pos):
        current_objective_index += 1
        if current_objective_index >= len(objectives):
            print("All objectives completed!")
            current_objective_index = 0  # Reset for replay

def main():
    global current_state

    while True:
        if current_state == MENU:
            handle_menu_events()
            draw_menu()
        elif current_state == PLAYING:
            handle_game_events()
            draw_game()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
