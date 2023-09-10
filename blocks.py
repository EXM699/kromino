import pygame


class Blocks(pygame.sprite.Sprite):
    RED = (255, 0, 0)
    BLACK = (0,0,0)
    def horizontalBlock(self,col1,col2,col3,x,y,hide = False):
        BORDERCOLOR = self.BLACK
        if self.focus:
            self.SQUAREBORDERSIZE = 30
            self.SQUAREBORDERSIZECONST = 30
        else:
            self.SQUAREBORDERSIZE = 27
            self.SQUAREBORDERSIZECONST = 27

        self.SQUARESIZECONST = 25
        if hide:
            self.SQUARESIZE = 0
            self.SQUAREBORDERSIZE = 0
        else:
            self.SQUARESIZE = 25

        margin = (self.SQUAREBORDERSIZE - self.SQUARESIZE) / 2
        lenBlock = (margin + self.SQUARESIZE + margin + self.SQUARESIZE + margin + self.SQUARESIZE + margin,
                    margin + self.SQUARESIZE + margin)
        self.surf = pygame.Surface(lenBlock)

        # draw border rectangle
        rectBorder = pygame.Rect(margin, margin, self.SQUAREBORDERSIZE, self.SQUAREBORDERSIZE)
        # draw the rectangles
        rect1 = pygame.Rect(margin, margin, self.SQUARESIZE, self.SQUARESIZE)
        rect2 = pygame.Rect(margin + self.SQUARESIZE + margin, margin, self.SQUARESIZE, self.SQUARESIZE)
        rect3 = pygame.Rect(margin + (self.SQUARESIZE + margin) * 2, margin, self.SQUARESIZE, self.SQUARESIZE)

        # Dessiner les rectangles sur l'écran
        pygame.draw.rect(self.surf, BORDERCOLOR, rectBorder)
        pygame.draw.rect(self.surf, col1, rect1)
        pygame.draw.rect(self.surf, col2, rect2)
        pygame.draw.rect(self.surf, col3, rect3)

        self.orientation = 'H'
        self.col1 = col1
        self.col2 = col2
        self.col3 = col3

        self.x = x
        self.y = y

        self.block = self.surf.get_rect()

    def verticalBlock(self,col1,col2,col3,x,y,hide=False):

        BORDERCOLOR = self.BLACK
        if self.focus:
            self.SQUAREBORDERSIZE = 30
            self.SQUAREBORDERSIZECONST = 30
        else:
            self.SQUAREBORDERSIZE = 27
            self.SQUAREBORDERSIZECONST = 27

        self.SQUARESIZECONST = 25
        if hide:
            self.SQUARESIZE = 0
            self.SQUAREBORDERSIZE = 0
        else:
            self.SQUARESIZE = 25

        margin = (self.SQUAREBORDERSIZE - self.SQUARESIZE) / 2
        lenBlock = (margin + self.SQUARESIZE + margin,
                    margin + self.SQUARESIZE + margin + self.SQUARESIZE + margin + self.SQUARESIZE + margin
                    )
        self.surf = pygame.Surface(lenBlock)

        # draw border rectangle
        rectBorder = pygame.Rect(margin, margin, self.SQUAREBORDERSIZE, self.SQUAREBORDERSIZE)
        # draw the rectangles
        rect1 = pygame.Rect(margin, margin, self.SQUARESIZE, self.SQUARESIZE)
        rect2 = pygame.Rect(margin,margin + self.SQUARESIZE + margin, self.SQUARESIZE, self.SQUARESIZE)
        rect3 = pygame.Rect(margin,margin + (self.SQUARESIZE + margin) * 2, self.SQUARESIZE, self.SQUARESIZE)

        # Dessiner les rectangles sur l'écran
        pygame.draw.rect(self.surf, BORDERCOLOR, rectBorder)
        pygame.draw.rect(self.surf, col1, rect1)
        pygame.draw.rect(self.surf, col2, rect2)
        pygame.draw.rect(self.surf, col3, rect3)

        self.orientation = 'V'
        self.col1 = col1
        self.col2 = col2
        self.col3 = col3

        self.x = x
        self.y = y

        self.block = self.surf.get_rect()


    def __init__(self,col1,col2,col3,posx = 0, posy=0):
        super(Blocks, self).__init__()
        self.SQUAREBORDERSIZEALIGN = 26

        self.isKilled = False
        self.hide = False
        self.focus = False
        self.canBeMoved = True
        self.orientation = None
        self.horizontalBlock(col1, col2, col3,posx,posy)


    def rectifPos(self,pos):
        #return pos

        diff = pos % self.SQUAREBORDERSIZEALIGN
        if diff > (self.SQUAREBORDERSIZEALIGN//2):
            newPos =  pos - diff + self.SQUAREBORDERSIZEALIGN
        else:
            newPos = pos - diff

        #return newPos - newPos % self.SQUAREBORDERSIZEALIGN
        return newPos

    # Move the sprite based on mouse motion
    def motionByMouse(self, rel):
        self.block.move_ip(rel)

    def setPosRectif (self,x,y):
        self.x = self.rectifPos(x)
        self.y = self.rectifPos(y)

    def setPos (self,x,y):
        self.x = x
        self.y = y

    def setPosXRectif(self, x):
        self.x = self.rectifPos(x)

    def setPosYRectif(self,  y):
        self.y = self.rectifPos(y)
    def setPosX(self, x):
        self.x = x

    def setPosY(self,  y):
        self.y = y

    def getPosX(self):
        return self.x

    def getPosY(self):
        return self.y

    def getPos(self):
        return(self.x,self.y)

    def rotate(self):
        if self.orientation == 'H':
            self.verticalBlock(self.col1,self.col2,self.col3,self.x,self.y)
            self.orientation = 'V'
        else:
            self.horizontalBlock(self.col3,self.col2,self.col1,self.x,self.y)
            self.orientation = 'H'

        self.block.x = self.x
        self.block.y = self.y

    def redraw(self):
        if self.orientation == 'V':
            self.verticalBlock(self.col1,self.col2,self.col3,self.x,self.y,self.hide)
        else:
            self.horizontalBlock(self.col1,self.col2,self.col3,self.x,self.y,self.hide)

        self.block.x = self.x
        self.block.y = self.y

    def setFocus(self,focus):
        self.focus = focus
        self.redraw()
class Bag():
    def setColor(self):
        self.color = []
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 255)
        YELLOW = (255, 255, 0)
        VIOLET = (127, 0, 255)

        self.color = [RED,GREEN,BLUE,YELLOW,VIOLET]

        return self.color
    def __init__(self):
        self.colors = self.setColor()
        self.bagBlocks = []

        for color in self.colors:
            self.bagBlocks.append(Blocks(color, color, color))

        for col1 in self.colors:
            for col2 in self.colors:
                for col3 in self.colors:
                        if Blocks(col1,col2,col3) not in self.bagBlocks and Blocks(col3,col2,col1) not in self.bagBlocks :
                            self.bagBlocks.append(Blocks(col1,col2,col3))



    def getBlock(self,index):
        return self.bagBlocks[index]

    def removeBlock(self,block):
        self.bagBlocks.remove(block)

    def getNumberBlock(self):
        return len(self.bagBlocks)