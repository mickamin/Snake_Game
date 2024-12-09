# Snake Game Implementation
import pygame

from direction import Direction
from game_state import GameState

# Initialize pygame
pygame.init()

# Game configuration
CUBE_SIZE = 25  # Size of each cube in the grid
CUBES_NUM = 20  # Number of cubes in one row/column
WIDTH = CUBE_SIZE * CUBES_NUM  # Screen width/height

# Setup display
screen = pygame.display.set_mode((WIDTH, WIDTH))

# Change the window title
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREY = (240, 240, 240)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Fill the screen with the background color
screen.fill(WHITE)
pygame.display.update()


def draw_grid():
    """Draw a grey grid on the background."""
    for x in range(0, WIDTH, CUBE_SIZE):
        pygame.draw.line(screen, GREY, (x, 0), (x, WIDTH))  # Vertical lines
    for y in range(0, WIDTH, CUBE_SIZE):
        pygame.draw.line(screen, GREY, (0, y), (WIDTH, y))  # Horizontal lines


def fill_bg():
    """Clears the screen and resets the background."""
    screen.fill(WHITE)
    draw_grid()


def splash_screen(screen, width):
    """Displays a splash screen for 1 second with an image and fade transition into the game."""
    # Load image for splash screen
    splash_image = pygame.image.load("Snake_Image.png")
    splash_image = pygame.transform.scale(
        splash_image, (width, width)
    )  # Scale the image to fit the screen

    draw_grid()

    # Display the splash image for 1 second
    screen.blit(splash_image, (0, 0))  # Draw the splash image
    pygame.display.update()  # Update the display

    start_time = pygame.time.get_ticks()  # Get current time
    while pygame.time.get_ticks() - start_time < 1000:  # Show for 1 second
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Allow quitting during splash
                pygame.quit()
                quit()

    # Now start fading the splash screen into the game grid
    fade_surface = pygame.Surface(
        (width, width)
    )  # Create a surface for the fade effect
    fade_surface.fill(
        (255, 255, 255)
    )  # Fill the surface with white (transition to game background)

    # Gradually fade out the splash screen and reveal the grid beneath
    for alpha in range(0, 255, 5):  # Gradually increase alpha from 0 to 255
        fade_surface.set_alpha(alpha)  # Set the fade surface alpha
        screen.blit(splash_image, (0, 0))  # Draw the splash image again
        screen.blit(fade_surface, (0, 0))  # Overlay the fade surface (increasing alpha)
        pygame.display.update()  # Update the display

        pygame.time.delay(10)  # Control the fade speed

    # Once fade-out is complete, ensure the grid is fully visible
    fill_bg()


# Drawing functions
def draw_snake_part(pos):
    """Draws a single part of the snake."""
    position = (pos.x * CUBE_SIZE, pos.y * CUBE_SIZE, CUBE_SIZE, CUBE_SIZE)
    pygame.draw.rect(screen, GREEN, position)


def draw_snake(snake):
    """Draws the entire snake."""
    for part in snake:
        draw_snake_part(part)


def draw_food(pos):
    """Draws the food on the screen."""
    radius = CUBE_SIZE // 2
    position = (pos.x * CUBE_SIZE + radius, pos.y * CUBE_SIZE + radius)
    pygame.draw.circle(screen, RED, position, radius)


def draw(snake, food):
    """Draws the current game state (snake and food)."""
    fill_bg()
    draw_snake(snake)
    draw_food(food)
    pygame.display.update()


# Main game loop
state = GameState(
    snake=None,
    direction=None,
    food=None,
    field_size=CUBES_NUM,
)
splash_screen(screen, WIDTH)

state.set_initial_position()

clock = pygame.time.Clock()

while True:
    clock.tick(8)  # Limit game loop to 10 frames per second

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            # Change direction based on arrow key input
            if event.key == pygame.K_LEFT:
                state.turn(Direction.LEFT)
            elif event.key == pygame.K_RIGHT:
                state.turn(Direction.RIGHT)
            elif event.key == pygame.K_UP:
                state.turn(Direction.UP)
            elif event.key == pygame.K_DOWN:
                state.turn(Direction.DOWN)

    state.step()  # Update game state
    draw(state.snake, state.food)  # Draw updated game state
