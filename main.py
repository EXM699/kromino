# Import the pygame module

import pygame
import random


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

if __name__ == "__main__":
    # Define constants for the screen width and height
    SCREEN_WIDTH = 1440
    SCREEN_HEIGHT = 900
    FPS = 30
    NBRBLOCKBYPLAYER = 9
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
        randomBlockId = random.randint(0, blocksInBag-1)
        player.append( bag.getBlock(randomBlockId))
        bag.removeBlock(bag.getBlock(randomBlockId))

    #create the blocks for the computer
    computer = []
    for i in range(NBRBLOCKBYPLAYER):
        blocksInBag = bag.getNumberBlock()
        randomBlockId = random.randint(0, blocksInBag-1)
        computer.append (bag.getBlock(randomBlockId))
        bag.removeBlock(bag.getBlock(randomBlockId))


    #create sprite group
    blocksGroup = pygame.sprite.Group()

    #put the first block in the middle of the board
    blockZero.block.x = blockZero.rectifPos(theBoard.boardTable.centerx)
    blockZero.block.y = blockZero.rectifPos(theBoard.boardTable.centery)
    blockZero.canBeMoved = False

    #show the blocks for the player
    """
    player[0].setPosX(0)
    player[0].setPosY(SCREEN_HEIGHT - 150)
    player[0].block.move_ip(player[0].getPos())
    player[0].canBeMoved = True
    """

    #blit the sceen
    screen.blit(theBoard.surf,theBoard.playGround)

    blocksGroup.add(blockZero)
    posXPlayer = 0
    posYPlayer = SCREEN_HEIGHT - 180
    for playerBlock in player:
        playerBlock.setPosX(posXPlayer)
        playerBlock.setPosY(posYPlayer)
        playerBlock.block.x = posXPlayer
        playerBlock.block.y = posYPlayer

        playerBlock.canBeMoved = True
        blocksGroup.add(playerBlock)
        posXPlayer += 100
        #screen.blit(playerBlock.surf, playerBlock.block)

    #for entity in blocksGroup:
    #    screen.blit(playerBlock.surf, entity.block)

    # Variable to keep the main loop running
    running = True

    clock = pygame.time.Clock()
    while running:
        movedBlock = None
        screen.fill(BACKGROUNDCOLOR)
        screen.blit(theBoard.surf, theBoard.playGround)
        mousePos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            for playerBlock in player:
                if event.type == MOUSEBUTTONDOWN and playerBlock.block.collidepoint(mousePos):
                    movedBlock = playerBlock.block
                    playerBlock.focus = True
                elif event.type == MOUSEBUTTONUP and playerBlock.focus :
                    playerBlock.focus = False
                    movedBlock = None

                    #rectif the x and y position only on the board
                    if theBoard.boardTable.collidepoint(mousePos):
                        xRectif = playerBlock.rectifPos(mousePos[0])
                        yRectif = playerBlock.rectifPos(mousePos[1])

                        canBeValidate = True
                        # can not overlap a block on the board
                        for blockBoard in board:
                            if playerBlock.block.colliderect(blockBoard.block):
                                canBeValidate = False

                        if canBeValidate:
                            playerBlock.setPosX(xRectif)
                            playerBlock.setPosY(yRectif)
                            #validation
                            #if validation ok remove from player or compyter and add to board
                    else:
                        playerBlock.setPosX(mousePos[0])
                        playerBlock.setPosY(mousePos[1])

                    playerBlock.block.x = playerBlock.getPosX()
                    playerBlock.block.y = playerBlock.getPosY()

                elif event.type == MOUSEMOTION and playerBlock.focus :
                    playerBlock.motionByMouse(event.rel)
                elif event.type == QUIT:
                    running = False


            #END FOR PLAYER
        #END FOR EVENT

        # Draw the player on the screen
        #screen.blit(blockZero.surf, blockZero.block)
        for entity in blocksGroup:
            screen.blit(entity.surf, entity.block)
        #END FOR

        # Update the display
        pygame.display.flip()

        clock.tick(FPS)

        # END WHILE

    #END __MAIN__
