# Import the pygame module

import pygame
import random
import time

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards

from pygame.locals import (
    QUIT,
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP,
    MOUSEMOTION,
)

import blocks
import playground

# Define constants for the screen width and height
SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 900
FPS = 30
NBRBLOCKBYPLAYER = 1
BACKGROUNDCOLOR = (250,233,217)

# Initialize pygame
pygame.init()


# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen = pygame.display.set_mode()
pygame.display.set_caption('CHROMINO')

#create playGround
theBoard = playground.PlayGround(SCREEN_WIDTH,SCREEN_HEIGHT)


# Instantiate a bag of blocks
bag = blocks.Bag()

#get randomly the first block to start the game
#always à 3 colors blocks
#always in the first 10 position in the bag
startBlockId = random.randint(0, 9)
blockZero = bag.getBlock(startBlockId)
bag.removeBlock(blockZero)


#create the board
board = []
board.append(blockZero)

#create the blocks for the player
player = []
for i in range(NBRBLOCKBYPLAYER):
    blocksInBag = bag.getNumberBlock()
    randomBlockId = random.randint(0, blocksInBag)
    player.append( bag.getBlock(randomBlockId))
    bag.removeBlock(bag.getBlock(randomBlockId))

#create the blocks for the computer
computer = []
for i in range(NBRBLOCKBYPLAYER):
    blocksInBag = bag.getNumberBlock()
    randomBlockId = random.randint(0, blocksInBag)
    computer.append (bag.getBlock(randomBlockId))
    bag.removeBlock(bag.getBlock(randomBlockId))


#create sprite group
blocksGroup = pygame.sprite.Group()

#put the first block in the middle of the board
blockZero.block.x = blockZero.rectifPos(theBoard.boardTable.centerx)
blockZero.block.y = blockZero.rectifPos(theBoard.boardTable.centery)
blockZero.canBeMoved = False

#show the blocks for the player

player[0].setPosX(0)
player[0].setPosY(SCREEN_HEIGHT - 150)
player[0].block.move_ip(player[0].getPos())
player[0].canBeMoved = True

#blit the sceen
screen.blit(theBoard.surf,theBoard.playGround)

blocksGroup.add(blockZero)
blocksGroup.add(player[0])

for entity in blocksGroup:
    screen.blit(entity.surf, entity.block)

# Variable to keep the main loop running
running = True

clock = pygame.time.Clock()
while running:
    screen.fill(BACKGROUNDCOLOR)
    screen.blit(theBoard.surf, theBoard.playGround)
    #pygame.display.flip()
    mousePos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        for playerBlock in player:
            if event.type == MOUSEBUTTONDOWN and playerBlock.block.collidepoint(mousePos):
                playerBlock.focus = True
            elif event.type == MOUSEBUTTONUP:
                playerBlock.focus = False
                playerBlock.setPosX(playerBlock.rectifPos(mousePos[0]))
                playerBlock.setPosY(playerBlock.rectifPos(mousePos[1]))
                playerBlock.block.x = playerBlock.getPosX()
                playerBlock.block.y = playerBlock.getPosY()
            elif event.type == MOUSEMOTION and playerBlock.focus:
                playerBlock.motionByMouse(event.rel)
            elif event.type == QUIT:
                running = False

            if playerBlock.block.colliderect(theBoard.boardTable):
                #print('je suis sur la table de jeu')
                pass

    #END WHILE

    # Draw the player on the screen
    #screen.blit(blockZero.surf, blockZero.block)
    for entity in blocksGroup:
        screen.blit(entity.surf, entity.block)

    # Update the display
    pygame.display.flip()

    clock.tick(FPS)



