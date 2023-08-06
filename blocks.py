import pygame


class Blocks(pygame.sprite.Sprite):
    def __init__(self,col1,col2,col3):
        BORDERCOLOR = (0,0,0)
        self.SQUAREBORDERSIZE = 27
        self.SQUARESIZE = 25

        super(Blocks, self).__init__()
        margin = (self.SQUAREBORDERSIZE - self.SQUARESIZE) / 2
        lenBlock = (margin + self.SQUARESIZE + margin + self.SQUARESIZE+margin+self.SQUARESIZE+margin, margin + self.SQUARESIZE + margin )
        self.surf = pygame.Surface(lenBlock)

        #draw border rectangle
        rectBorder = pygame.Rect(margin, margin, self.SQUAREBORDERSIZE, self.SQUAREBORDERSIZE)
        # Dessiner les rectangles
        rect1 = pygame.Rect(margin, margin, self.SQUARESIZE, self.SQUARESIZE)
        rect2 = pygame.Rect(margin + self.SQUARESIZE + margin, margin, self.SQUARESIZE, self.SQUARESIZE)
        rect3 = pygame.Rect(margin + (self.SQUARESIZE + margin) * 2, margin, self.SQUARESIZE, self.SQUARESIZE)

        # Dessiner les rectangles sur l'écran
        pygame.draw.rect(self.surf, BORDERCOLOR, rectBorder)
        pygame.draw.rect(self.surf, col1, rect1)
        pygame.draw.rect(self.surf, col2, rect2)
        pygame.draw.rect(self.surf, col3, rect3)

        self.block = self.surf.get_rect()
        self.focus = False
        self.canBeMoved = True

        self.col1 = col1
        self.col2 = col2
        self.col3 = col3

    def rectifPos(self,pos):
        diff = pos % self.SQUAREBORDERSIZE
        return pos - diff

    # Move the sprite based on mouse motion
    def motionByMouse(self, rel):
        self.block.move_ip(rel)

    def setPos (self,x,y):
        self.x = self.rectifPos(x)
        self.y = self.rectifPos(y)

    def setPosX(self, x):
        self.x = self.rectifPos(x)

    def setPosY(self,  y):
        self.y = self.rectifPos(y)

    def getPosX(self):
        return self.x

    def getPosY(self):
        return self.y

    def getPos(self):
        return(self.x,self.y)
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

        for i in range(100): #just for the dev period
            #Three time the same color
            for color in self.colors:
                self.bagBlocks.append(Blocks(color, color, color))
                self.bagBlocks.append(Blocks(color, color, color))

        #Twice the same color

        #Three different color


    def getBlock(self,index):
        return self.bagBlocks[index]

    def removeBlock(self,block):
        self.bagBlocks.remove(block)

    def getNumberBlock(self):
        return len(self.bagBlocks)