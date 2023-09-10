# Import the pygame module
import time

import pygame
import random
import datetime

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

def timing(func):
    def inner(*args,**kwargs):
        print('******************* '+func.__name__+' *******************' )
        ct = datetime.datetime.now()
        print("current time:-", ct)
        result = func(*args,**kwargs)
        ct = datetime.datetime.now()
        print("current time:-", ct)
        return  result
    return inner

def moveAllSpriteBoard(direction,board):
    global xRectifCoef
    global yRectifCoef

    if direction == 'U':
        yRectifCoef = yRectifCoef + 1

    if direction == 'D':
        yRectifCoef = yRectifCoef - 1

    if direction == 'L':
        xRectifCoef = xRectifCoef + 1

    if direction == 'R':
        xRectifCoef = xRectifCoef - 1

    for block in board:
        if direction == 'U':
            block.setPosXRectif(block.x)
            block.setPosYRectif(block.y - block.SQUAREBORDERSIZECONST)
            #block.redraw()

        if direction == 'D':
            block.setPosXRectif(block.x)
            block.setPosYRectif(block.y + block.SQUAREBORDERSIZECONST)
            #block.redraw()

        if direction == 'L':
            block.setPosYRectif(block.y)
            block.setPosXRectif(block.x - block.SQUAREBORDERSIZECONST)
            #block.redraw()

        if direction == 'R':
            block.setPosYRectif(block.y)
            block.setPosXRectif(block.x + block.SQUAREBORDERSIZECONST)

        if block.orientation == 'H':
            print(block.y)
            if (block.x + (3 * theBoard.rectsize) < theBoard.boardTable.size[0] and block.y < theBoard.boardTable.size[1]\
                    and (block.y > 127)):
                block.hide = False
            else:
                block.hide = True

        if block.orientation == 'V':
            if block.x  < theBoard.boardTable.size[0] and block.y + (3 * theBoard.rectsize) < theBoard.boardTable.size[1]\
                    and (block.y > 127):
                block.hide = False
            else:
                block.hide = True

        block.redraw()


def addToMatrix(matrix,block):
    global minX
    global maxX
    global minY
    global maxY

    x = int(block.x/theBoard.rectsize + MATRIXCOEF + xRectifCoef)
    y = int(block.y/theBoard.rectsize + MATRIXCOEF + yRectifCoef)
    xOrig = x
    yOrig = y

    matrix[x][y]=block.col1

    if block.orientation == 'H':
        if x < minX or minX == 0:
            minX = xOrig

        if x + 2 > maxX or minX == 0:
            maxX = x + 2

        if y < minY or minY == 0:
            minY = yOrig
        elif y > maxY or minX == 0:
            maxY = yOrig

        x = x + 1
        matrix[x][y] = block.col2
        x = x + 1
        matrix[x][y] = block.col3

    else:

        if x < minX or minX == 0:
            minX = x
        elif x > maxX or minX == 0:
            maxX = x

        if y < minY or minY == 0:
            minY = y

        if y+2 > maxY or minY == 0:
            maxY = y + 2

        y = y + 1
        matrix[x][y] = block.col2
        y = y + 1
        matrix[x][y] = block.col3

    if maxY ==0:
        maxY = minY

def transScreenPosMatPosX(x):
    x = int((x / theBoard.rectsize) + MATRIXCOEF)
    return x + xRectifCoef

def transScreenPosMatPosY(y):
    y = int((y / theBoard.rectsize) + MATRIXCOEF)
    return y +  yRectifCoef

def checkBlockArround(matrix,color,x,y):
    val = 0
    # curent pos
    x = int(x)
    y = int(y)
    if matrix[x][y] != 0:
        return -1

    # left
    #if matrix[x-1][ y] != 0:
    #    return -1

    if matrix[x-1][ y] == color:
        val = val + 1

    if matrix[x-1][y] != color and matrix[x-1][ y] != 0:
        return - 1

    # up
    #if matrix[x ][ y-1] != 0:
    #    return -1

    if matrix[x ][ y-1] == color:
        val = val + 1

    if matrix[x][ y-1] != color and matrix[x][ y-1] != 0:
        return - 1


    # right
    #if matrix[x + 1][ y] != 0:
    #    return -1

    if matrix[x+1][ y] == color:
        val = val + 1

    if matrix[x+1][ y] != color and matrix[x+1][ y] != 0:
        return - 1

    # down
    #if matrix[x ][ y + 1] != 0:
    #    return -1

    if matrix[x][ y+1] == color:
        val = val + 1

    if matrix[x][ y+1] != color and matrix[x][ y+1] != 0:
        return - 1

    return val

def validationBlockV(matrix,block,x,y):
    val = 0
    rep = checkBlockArround(matrix, block.col1,int(x),int(y))

    if rep == -1:
        return False
    else:
        val = val + rep

    rep = checkBlockArround(matrix, block.col2, int(x ), int(y+1))

    if rep == -1:
        return False
    else:
        val = val + rep

    rep =  checkBlockArround(matrix, block.col3, int(x ), int(y+2))

    if rep == -1:
        return False
    else:
        val = val + rep

    return val > 1

def validationBlockH(matrix, block, x, y):
    val = 0

    rep = checkBlockArround(matrix, block.col1, int(x), int(y))

    if rep == -1:
        return False
    else:
        val = val + rep

    rep = checkBlockArround(matrix, block.col2, int(x+1) , int(y))

    if rep == -1:
        return False
    else:
        val = val + rep

    rep = checkBlockArround(matrix, block.col3, int(x+2) , int(y))

    if rep == -1:
        return False
    else:
        val = val + rep

    return val > 1

def validationBlock(matrix,block,x,y):
    if block.orientation == 'H':
        return validationBlockH(matrix, block, x, y)

    if block.orientation == 'V':
        return validationBlockV(matrix, block, x, y)


def computerIA(matrix, computer, minX, maxX, minY, maxY):

    blockOk = False
    find = False
    for block in computer:
        i = 0
        while i <= 3 and not find:
            x = minX - 2
            while x <= maxX + 2 and not find:
                x = x + 1
                y = minY - 2

                while y <= maxY + 2 and  not find:
                    y = y + 1
                    if (block.orientation == 'H' and matrix[x][y] == 0 and matrix[x+1][y] == 0 and matrix[x+2][y] == 0 ) or \
                            (block.orientation == 'V' and matrix[x][y] == 0 and matrix[x][y+1] == 0 and matrix[x][y+2] == 0 ):
                        blockOk = validationBlock(matrix,block,x,y)
                    if blockOk:
                        find = True

            if not find:
                block.rotate()
                i = i + 1

        if find:
            break

    if blockOk:
        rect = pygame.Rect(SCREEN_WIDTH / 2 - 200, SCREEN_HEIGHT / 2 - 300, 50, 50)

        icon = pygame.image.load('./assets/reflechir.png')
        icon = pygame.transform.scale(icon, (50, 50))

        # surface.blit(self.icon, self.rect)
        screen.blit(icon, rect)
        pygame.display.flip()
        # pygame.display.flip()
        time.sleep(2)

        calculX = ((x - MATRIXCOEF) * theBoard.rectsize) - (xRectifCoef * theBoard.rectsize)
        calculY = ((y - MATRIXCOEF) * theBoard.rectsize) - (yRectifCoef * theBoard.rectsize)

        block.setPosX(calculX)
        block.setPosY(calculY)
        addToMatrix(gameMatrix, block)
        computer.remove(block)
        board.append(block)
        block.redraw()
        blocksGroup.add(block)

    else:
        blocksInBag = bag.getNumberBlock()
        randomBlockId = random.randint(0, blocksInBag - 1)
        computer.append(bag.getBlock(randomBlockId))
        bag.removeBlock(bag.getBlock(randomBlockId))
        rect = pygame.Rect(SCREEN_WIDTH / 2 - 200, SCREEN_HEIGHT / 2 - 300, 50, 50)

        icon = pygame.image.load('./assets/IA_takes.png')
        icon = pygame.transform.scale(icon, (400, 400))

        # surface.blit(self.icon, self.rect)
        screen.blit(icon, rect)
        pygame.display.flip()
        time.sleep(3)

def findFreeSpace(x = None, y = None):
    print(' -----> findFreeSpece '+str(x)+' '+str(y))
    if x is None:
        x = theBoard.playerTable.x
    if y is None:
        y = theBoard.playerTable.y

    for blockPlayer in player:
        if blockPlayer.x == x and blockPlayer.y == y:
            x = (x + blockPlayer.SQUAREBORDERSIZE * 3) + 5
            print('new x '+str(x))
            if x > theBoard.playerTable.width:
                print('out off width')
                x = 0
                y = y + blockPlayer.SQUAREBORDERSIZE + 5
                return findFreeSpace(x, y)
                break

            if y > screen.get_height():
                x = theBoard.playerTable.x
                y = theBoard.playerTable.y
                print('out of borad then in corener')
                break

            print('recall findfreespace')
            return findFreeSpace(x,y)
            break

    return (x,y)

if __name__ == "__main__":
    # Define constants for the screen width and height
    xRectifCoef = 0
    yRectifCoef = 0

    MATRIXCOEF = 100
    #SCREEN_WIDTH = 1440
    #SCREEN_HEIGHT = 900
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
    SCREEN_WIDTH = screen.get_width()
    SCREEN_HEIGHT = screen.get_height()
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

    #put the first block in the middle of the board
    blockZero.block.x = blockZero.rectifPos(theBoard.boardTable.centerx)
    blockZero.block.y = blockZero.rectifPos(theBoard.boardTable.centery)
    blockZero.setPosX(blockZero.block.x)
    blockZero.setPosY(blockZero.block.y)
    blockZero.canBeMoved = False

    #create MBR
    #minX = blockZero.x
    #maxX = blockZero.x + 3
    #minY = blockZero.y
    #maxY = blockZero.y + 3

    minX = 0
    maxX = 0
    minY = 0
    maxY = 0

    #create the board
    board = []
    board.append(blockZero)

    #create the blocks for the player
    player = []
    for i in range(NBRBLOCKBYPLAYER):
        blocksInBag = bag.getNumberBlock()
        randomBlockId = random.randint(0, blocksInBag-1)
        player.append(bag.getBlock(randomBlockId))
        bag.removeBlock(bag.getBlock(randomBlockId))

    #create the blocks for the computer
    computer = []
    for i in range(NBRBLOCKBYPLAYER):
        blocksInBag = bag.getNumberBlock()
        randomBlockId = random.randint(0, blocksInBag-1)
        computer.append (bag.getBlock(randomBlockId))
        bag.removeBlock(bag.getBlock(randomBlockId))

    gameMatrix = [[0 for _ in range(1000)] for _ in range(1000)]

    addToMatrix(gameMatrix,blockZero)

    #create sprite group
    blocksGroup = pygame.sprite.Group()


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

    #to debug IA

    """
    posXComputer = SCREEN_WIDTH - 180
    posYComputer = 0
    for playerComputer in computer:
        playerComputer.setPosX(posXComputer)
        playerComputer.setPosY(posYComputer)
        playerComputer.block.x = posXComputer
        playerComputer.block.y = posYComputer

        playerComputer.canBeMoved = False
        blocksGroup.add(playerComputer)
        posYComputer += 30
    """
    ##########

    # Variable to keep the main loop running
    running = True

    clock = pygame.time.Clock()
    captured = False
    arrowCaptured = False
    addBlock = False
    turn = 'PLAYER'

    #playground.Button.draw(theBoard.surf)



    while running and computer and player and bag :
        if turn == 'COMPUTER':
            computerIA(gameMatrix, computer, minX, maxX, minY, maxY)
            turn = 'PLAYER'

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
                            #validation

                            if validationBlock(gameMatrix,playerBlock,transScreenPosMatPosX(xRectif),transScreenPosMatPosY(yRectif)):
                                playerBlock.setPosXRectif(xRectif)
                                playerBlock.setPosYRectif(yRectif)
                                board.append(playerBlock)
                                addToMatrix(gameMatrix, playerBlock)
                                player.remove(playerBlock)
                                turn = 'COMPUTER'
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

                elif event.type == MOUSEBUTTONDOWN and not captured and \
                        theBoard.buttonAdd.collidepoint(mousePos) and \
                        not arrowCaptured and not addBlock:
                    addBlock = True

                    blocksInBag = bag.getNumberBlock()
                    randomBlockId = random.randint(0, blocksInBag - 1)
                    tempoBlock = bag.getBlock(randomBlockId)
                    posInPlayerTable = findFreeSpace()
                    print('je set la position ')
                    print(posInPlayerTable)
                    tempoBlock.setPosX(posInPlayerTable[0])
                    tempoBlock.setPosY(posInPlayerTable[1])
                    player.append(tempoBlock)
                    blocksGroup.add(tempoBlock)
                    bag.removeBlock(tempoBlock)
                    turn = 'COMPUTER'
                    tempoBlock.redraw()

                elif event.type == MOUSEBUTTONUP and not captured and \
                        theBoard.buttonAdd.collidepoint(mousePos) and \
                        not arrowCaptured and addBlock:
                    addBlock = False

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

    if  not computer:
        rect = pygame.Rect(SCREEN_WIDTH / 2 - 200, SCREEN_HEIGHT / 2 - 300, 50, 50)

        endGame = pygame.image.load('./assets/you_win.png')
        endGame = pygame.transform.scale(endGame, (400, 200))

        # surface.blit(self.icon, self.rect)
        screen.blit(endGame, rect)
        pygame.display.flip()
        # pygame.display.flip()
        time.sleep(4)



    if not player:

        rect = pygame.Rect(SCREEN_WIDTH / 2 - 200, SCREEN_HEIGHT / 2 - 300, 50, 50)

        endGame = pygame.image.load('./assets/you_lose.png')
        endGame = pygame.transform.scale(endGame, (400, 200))

        # surface.blit(self.icon, self.rect)
        screen.blit(endGame, rect)
        pygame.display.flip()
        # pygame.display.flip()
        time.sleep(4)

    if  not bag:
        rect = pygame.Rect(SCREEN_WIDTH / 2 - 200, SCREEN_HEIGHT / 2 - 300, 50, 50)

        endGame = pygame.image.load('./assets/game_over.png')
        endGame = pygame.transform.scale(endGame, (400, 200))

        # surface.blit(self.icon, self.rect)
        screen.blit(endGame, rect)
        pygame.display.flip()
        # pygame.display.flip()
        time.sleep(4)

    #END __MAIN__
