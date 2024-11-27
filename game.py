# Creating Snake Game
import pygame.display
import pygame

# Initializing pygame
pygame.init()

#Defining the game window parameters
CUBE_SIZE = 25
CUBES_NUM = 20
WIDTH = CUBE_SIZE * CUBES_NUM
screen = pygame.display.set_mode((WIDTH, WIDTH))

#Defining colours
WHITE = (255, 255, 255)
BLUE  = (0, 0, 255)
GREEN = (0, 255, 0)

# Filling the screen with the background color
screen.fill(WHITE)
pygame.display.update()

# Main game loop to keep the window open
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                quit()