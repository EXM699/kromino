# Import the pygame module

import pygame
from pygame import draw, sprite, FULLSCREEN
from pygame.draw import rect

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP,
    MOUSEMOTION,
)

import blocks

# Define constants for the screen width and height

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'


# Initialize pygame

pygame.init()


# Create the screen object

# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),FULLSCREEN)
screen = pygame.display.set_mode()
pygame.display.set_caption('KROMINO')

# Instantiate player. Right now, this is just a rectangle.
#player = Player()
player = blocks.Blocks()

# Variable to keep the main loop running

running = True

clock = pygame.time.Clock()
#squares = pygame.sprite.Group(player.rect)
#squares.add(player.rect)

# Main loop
while running:
    # for loop through the event queue
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == MOUSEBUTTONDOWN and player.block.collidepoint(mouse_pos):
            #print('mouse down')
            player.focus = True
        elif event.type == MOUSEBUTTONUP:
            player.focus = False
        elif event.type == MOUSEMOTION and player.focus:
            player.motionByMouse(event.rel)


        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False
        # Get all the keys currently pressed

    #pressed_keys = pygame.key.get_pressed()


    # Update the player sprite based on user keypresses

    #player.update(pressed_keys)

    # Fill the screen with black
    screen.fill((0, 0, 0))


    # Draw the player on the screen
    #screen.blit(player.surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

    screen.blit(player.surf, player.block)

    # Update the display
    pygame.display.flip()

    clock.tick(30)