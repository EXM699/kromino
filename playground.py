import pygame

class PlayGround(pygame.sprite.Sprite):

    def loadImage(self,pathImage):
        return pygame.image.load(pathImage)
    def __init__(self,screenwidth,screenhight):

        super(PlayGround, self).__init__()
        self.rectsize = 26
        self.surf = pygame.Surface((screenwidth,screenhight))

        # Draw the 3 zones
        self.boardTable = pygame.Rect(0, 0, screenwidth - 200, screenhight - 250)
        self.score = pygame.Rect(screenwidth - 200, 0, 200, screenhight - 250)
        self.playerTable = pygame.Rect(0, screenhight - 250,screenwidth , 250)


        #arrowRightImage = self.loadImage('./assets/arrow_right.png')

        self.buttonUp = self.button(screenwidth - 300, screenhight - 400,self.rectsize,self.rectsize)
        self.buttonDown = self.button(screenwidth - 300, screenhight - 350,self.rectsize,self.rectsize)
        self.buttonLeft = self.button(screenwidth - 350, screenhight - 375,self.rectsize,self.rectsize)
        self.buttonRight = self.button(screenwidth - 250, screenhight - 375,self.rectsize,self.rectsize)
        self.buttonAdd = self.button(screenwidth - 100, screenhight - 375,self.rectsize * 3,self.rectsize * 3)

        pygame.draw.rect(self.surf, (63,124,182), self.boardTable)

        iter = screenhight // self.rectsize
        for i in range(iter - 1):
            y = self.rectsize + self.rectsize * i
            pygame.draw.line(self.surf,(255,255,255),(0,y),(screenwidth,y))


        iter = screenwidth // self.rectsize
        for i in range(iter - 1):
            x = self.rectsize + self.rectsize * i
            pygame.draw.line(self.surf,(255,255,255),(x,0),(x,screenhight))


        pygame.draw.rect(self.surf, (255, 0, 0), self.score)
        pygame.draw.rect(self.surf, (255, 0, 255), self.playerTable)

        pygame.draw.rect(self.surf, (220, 220, 225), self.buttonUp)
        pygame.draw.rect(self.surf, (220, 220, 220), self.buttonLeft)
        pygame.draw.rect(self.surf, (220, 220, 220), self.buttonRight)
        pygame.draw.rect(self.surf, (220, 220, 220), self.buttonDown)
        pygame.draw.rect(self.surf, (220, 220, 220), self.buttonAdd)


        #self.surf.blit(arrowRightImage, (screenwidth - 250, screenhight - 375))

        self.playGround = self.surf.get_rect()


    def button(self,x,y,sizeX,sizeY):
        #image = pygame.image.load ('./assets/arrow_right.png').convert()
        #self.buttonRect = image.get_rect()
        self.buttonRect = pygame.Rect(x, y, sizeX, sizeY)
        #self.buttonRect.x = x
        #self.buttonRect.y = y
        #self.buttonRect.size((sizeX,sizeY))
        return self.buttonRect
