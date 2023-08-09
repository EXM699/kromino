# Import the pygame module

import pygame
import random
import array

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



def moveAllSpriteBoard(direction,board):
    global xRectifCoef
    global yRectifCoef
    for block in board:
        if direction == 'U':
            yRectifCoef = yRectifCoef + 1
            block.setPosXRectif(block.x)
            block.setPosYRectif(block.y - block.SQUAREBORDERSIZE)
            block.redraw()

        if direction == 'D':
            yRectifCoef = yRectifCoef - 1
            block.setPosXRectif(block.x)
            block.setPosYRectif(block.y + block.SQUAREBORDERSIZE)
            block.redraw()

        if direction == 'L':
            xRectifCoef = xRectifCoef - 1
            block.setPosYRectif(block.y)
            block.setPosXRectif(block.x - block.SQUAREBORDERSIZE)
            block.redraw()

        if direction == 'R':
            xRectifCoef = xRectifCoef + 1
            block.setPosYRectif(block.y)
            block.setPosXRectif(block.x + block.SQUAREBORDERSIZE)
            block.redraw()

def addToMatrix(matrix,posX,posY,color):
    #print(color)
    #print(int(posX/theBoard.rectsize + MATRIXCOEF))
    matrix[int(posX/theBoard.rectsize + MATRIXCOEF)][int(posY/theBoard.rectsize + MATRIXCOEF)]=color



if __name__ == "__main__":
    # Define constants for the screen width and height
    xRectifCoef = 0
    yRectifCoef = 0

    MATRIXCOEF = 100
    SCREEN_WIDTH = 1440
    SCREEN_HEIGHT = 900
    FPS = 30
    NBRBLOCKBYPLAYER = 9
    BACKGROUNDCOLOR = (0,0,0)

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

    gameMatrix = [[0 for _ in range(1000)] for _ in range(1000)]


    #create sprite group
    blocksGroup = pygame.sprite.Group()

    #put the first block in the middle of the board
    blockZero.block.x = blockZero.rectifPos(theBoard.boardTable.centerx)
    blockZero.block.y = blockZero.rectifPos(theBoard.boardTable.centery)
    blockZero.setPosX(blockZero.block.x)
    blockZero.setPosY(blockZero.block.y)
    blockZero.canBeMoved = False

    addToMatrix(gameMatrix, blockZero.x, blockZero.y, blockZero.col1)

    print(gameMatrix[124][112])

    #for row in gameMatrix:
    #    print(row)


    print(blockZero.block.x/theBoard.rectsize + MATRIXCOEF)
    print(blockZero.block.y/theBoard.rectsize + MATRIXCOEF)

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

    # Variable to keep the main loop running
    running = True

    clock = pygame.time.Clock()
    captured = False
    arrowCaptured = False

    while running:
        #movedBlock = None

        screen.fill(BACKGROUNDCOLOR)
        screen.blit(theBoard.surf, theBoard.playGround)
        mousePos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            for playerBlock in player:
                if event.type == MOUSEBUTTONDOWN and playerBlock.block.collidepoint(mousePos) and not captured:
                    playerBlock.setFocus(True)
                    captured = True
                    pygame.mouse.set_pos(playerBlock.getPos())
                elif event.type == MOUSEBUTTONDOWN and playerBlock.focus and captured:
                    captured = False
                    playerBlock.setFocus(False)
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
                            playerBlock.setPosXRectif(xRectif)
                            playerBlock.setPosYRectif(yRectif)
                            #validation
                            #if validation ok remove from player or compyter and add to board and focus = False
                            board.append(playerBlock)
                            player.remove(playerBlock)
                    else:
                        playerBlock.setPosX(mousePos[0])
                        playerBlock.setPosY(mousePos[1])

                    playerBlock.block.x = playerBlock.getPosX()
                    playerBlock.block.y = playerBlock.getPosY()

                elif event.type == pygame.KEYDOWN and playerBlock.focus:
                    # Check if the key pressed is 'r'
                    if event.key == pygame.K_r:
                        playerBlock.rotate()
                        playerBlock.setFocus(False)
                        captured = False

                elif event.type == MOUSEMOTION and playerBlock.focus:
                    playerBlock.motionByMouse(event.rel)

                elif event.type == MOUSEBUTTONDOWN and \
                        not captured and not arrowCaptured and theBoard.buttonUp.collidepoint(mousePos):
                    arrowCaptured = True

                elif event.type == MOUSEBUTTONUP and \
                        not captured and \
                        theBoard.buttonUp.collidepoint(mousePos) and \
                        arrowCaptured:
                    arrowCaptured = False
                    moveAllSpriteBoard('U', board)

                elif event.type == MOUSEBUTTONDOWN and \
                        not captured and not arrowCaptured and theBoard.buttonDown.collidepoint(mousePos):
                    arrowCaptured = True

                elif event.type == MOUSEBUTTONUP and \
                        not captured and \
                        theBoard.buttonDown.collidepoint(mousePos) and \
                        arrowCaptured:
                    arrowCaptured = False
                    moveAllSpriteBoard('D', board)

                elif event.type == MOUSEBUTTONDOWN and \
                        not captured and not arrowCaptured and theBoard.buttonLeft.collidepoint(mousePos):
                    arrowCaptured = True

                elif event.type == MOUSEBUTTONUP and \
                        not captured and \
                        theBoard.buttonLeft.collidepoint(mousePos) and \
                        arrowCaptured:
                    arrowCaptured = False
                    moveAllSpriteBoard('L', board)

                elif event.type == MOUSEBUTTONDOWN and \
                        not captured and not arrowCaptured and theBoard.buttonRight.collidepoint(mousePos):
                    arrowCaptured = True

                elif event.type == MOUSEBUTTONUP and \
                        not captured and \
                        theBoard.buttonRight.collidepoint(mousePos) and \
                        arrowCaptured:
                    arrowCaptured = False
                    moveAllSpriteBoard('R', board)


                elif event.type == QUIT:
                    running = False


            #END FOR PLAYER
        #END FOR EVENT

        # Draw the player on the screen
        for entity in blocksGroup:
            screen.blit(entity.surf, entity.block)

        #END FOR

        # Update the display
        pygame.display.flip()

        clock.tick(FPS)

        # END WHILE

    #END __MAIN__
