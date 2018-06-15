# import the pygame module, and the
# sys module for exiting the window we create
import pygame, sys

# import some useful constants
from pygame.locals import *

DIRT = 0
GRASS = 1
WATER = 2
COAL = 3

# color
BLACK = (0, 0, 0)
BROWN = (153, 76, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# useful game dimentions
TILE_SIZE = 40
MAP_WIDTH = 5
MAP_HEIGHT = 5

# a list representing our tilemap
tilemap = [
    [GRASS, COAL, DIRT,DIRT,WATER],
    [WATER, WATER, GRASS,COAL,GRASS],
    [COAL, WATER, GRASS,DIRT,GRASS],
    [WATER, DIRT, DIRT,DIRT,DIRT],
    [WATER, COAL, GRASS,DIRT,GRASS],
    [DIRT, COAL, WATER,GRASS,WATER]
]

colors = {
    DIRT: BROWN,
    GRASS: GREEN,
    WATER: BLUE,
    COAL: BROWN
}

# initialise the pygame module
pygame.init()

# create a new drawing surface, width=300, height=300
DISPLAYSURF = pygame.display.set_mode((MAP_WIDTH * TILE_SIZE, MAP_HEIGHT * TILE_SIZE))
# give the window a caption
pygame.display.set_caption('My First Game')

# loop (repeat) forever
while True:

    # get all the user events
    for event in pygame.event.get():
        print(event)
        # if the user wants to quit
        if event.type == QUIT:
            # end the game and close the window
            pygame.quit()
            sys.exit()

    for row in range(MAP_HEIGHT):
        for column in range(MAP_WIDTH):
            pygame.draw.rect(DISPLAYSURF, colors[tilemap[row][column]],
                             (column * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # update the display
    pygame.display.update()
