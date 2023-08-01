# Import the pygame module

import pygame
import random

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
FPS = 30


# Initialize pygame
pygame.init()


# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#screen = pygame.display.set_mode()
pygame.display.set_caption('CHROMINO')

# Instantiate a bag of blocks
bag = blocks.Bag()

#get randomly the first block to start the game
#always à 3 colors blocks
#always in the first 10 position in the bag
startBlockId = random.randint(1, 10)
blockZero = bag.getBlock(startBlockId)
bag.removeBlock(blockZero)

#put the first block in the middle of the screen
blockZero.block.move_ip((SCREEN_WIDTH/2, SCREEN_HEIGHT/2))


# Variable to keep the main loop running
running = True

clock = pygame.time.Clock()
while running:

    mouse_pos = pygame.mouse.get_pos()
    #print(mouse_pos)
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN and blockZero.block.collidepoint(mouse_pos):
            blockZero.focus = True
        elif event.type == MOUSEBUTTONUP:
            blockZero.focus = False
        elif event.type == MOUSEMOTION and blockZero.focus:
            blockZero.motionByMouse(event.rel)
        elif event.type == QUIT:
            running = False


    screen.fill((0, 0, 0))

    # Draw the player on the screen
    screen.blit(blockZero.surf, blockZero.block)

    # Update the display
    pygame.display.flip()

    clock.tick(FPS)


"""
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
            #player.focus = True
            pass
        elif event.type == MOUSEBUTTONUP:
            #player.focus = False
            pass
        elif event.type == MOUSEMOTION :
        #and player.focus:
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

"""

