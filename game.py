# Creating Snake Game
import pygame
import pygame.display

# Initializing pygame
pygame.init()

# Defining the game window parameters
CUBE_SIZE = 25
CUBES_NUM = 20
WIDTH = CUBE_SIZE * CUBES_NUM
screen = pygame.display.set_mode((WIDTH, WIDTH))

# Defining colours
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Filling the screen with the background color (white)
screen.fill(WHITE)
pygame.display.update()


# Drawing the snake elements
def draw_snake_part(pos):
    position = (pos.x * CUBE_SIZE, pos.y * CUBE_SIZE, CUBE_SIZE, CUBE_SIZE)
    pygame.draw.rect(screen, GREEN, position)
    pygame.display.update()


# Drawing the full snake
def draw_snake(snake):
    for part in snake:
        draw_snake_part(part)


# Drawing the food
def draw_food(pos):
    radius = float(CUBE_SIZE) / 2
    position = (pos.x * CUBE_SIZE + radius, pos.y * CUBE_SIZE + radius)
    pygame.draw.circle(screen, BLUE, position, radius)
    pygame.display.update()


# Clearing the screen and reset the background
def fill_bg():
    screen.fill(WHITE)


# Drawing the current game state (snake and food)
def draw(snake, food):
    fill_bg()
    draw_snake(snake)
    draw_food(food)
    pygame.display.update()


# Main game loop to keep the window open
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
