import pygame
from pygame import event



class Blocks(pygame.sprite.Sprite):
    def __init__(self,col1,col2,col3):
        super(Blocks, self).__init__()
        square_size = 25
        margin = 0
        lenBlock = ((square_size + margin) * 3, square_size)
        self.surf = pygame.Surface(lenBlock)

        # Dessiner les rectangles
        rect1 = pygame.Rect(margin, margin, square_size, square_size)
        rect2 = pygame.Rect(margin + square_size + margin, margin, square_size, square_size)
        rect3 = pygame.Rect(margin + (square_size + margin) * 2, margin, square_size, square_size)

        # Dessiner les rectangles sur l'écran
        pygame.draw.rect(self.surf, col1, rect1)  # Rouge
        pygame.draw.rect(self.surf, col2, rect2)  # Bleu
        pygame.draw.rect(self.surf, col3, rect3)  # Vert

        self.block = self.surf.get_rect()
        self.focus = False
        self.canBeMoved = True

    # Move the sprite based on mouse motion
    def motionByMouse(self, rel):
        self.block.move_ip(rel)

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

        #Three time the same color
        for color in self.colors:
            self.bagBlocks.insert(1, Blocks(color, color, color))
            self.bagBlocks.insert(1, Blocks(color, color, color))

        #Twice the same color

        #Three different color


    def getBlock(self,index):
        return self.bagBlocks[index]

    def removeBlock(self,block):
        self.bagBlocks.remove(block)

    def getNumberBlock(self):
        return len(self.bagBlocks)