import pygame

class PlayGround(pygame.sprite.Sprite):
    def __init__(self,screenwidth,screenhight):

        super(PlayGround, self).__init__()
        self.rectsize = 26
        self.surf = pygame.Surface((screenwidth,screenhight))

        # Draw the 3 zones
        self.boardTable = pygame.Rect(0, 0, screenwidth - 200, screenhight - 250)
        self.score = pygame.Rect(screenwidth - 200, 0, 200, screenhight - 250)
        self.playerTable = pygame.Rect(0, screenhight - 250,screenwidth , 250)

        self.buttonUp = self.button(screenwidth - 300, screenhight - 400,self.rectsize,self.rectsize)
        self.buttonDown = self.button(screenwidth - 300, screenhight - 350,self.rectsize,self.rectsize)
        self.buttonLeft = self.button(screenwidth - 350, screenhight - 375,self.rectsize,self.rectsize)
        self.buttonRight = self.button(screenwidth - 250, screenhight - 375,self.rectsize,self.rectsize)
        self.buttonAdd = self.button(screenwidth - 100, screenhight - 375,self.rectsize * 3,self.rectsize * 3)

        pygame.draw.rect(self.surf, (255,255,0), self.boardTable)

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

        pygame.draw.rect(self.surf, (220, 220, 220), self.buttonUp)
        pygame.draw.rect(self.surf, (220, 220, 220), self.buttonLeft)
        pygame.draw.rect(self.surf, (220, 220, 220), self.buttonRight)
        pygame.draw.rect(self.surf, (220, 220, 220), self.buttonDown)
        pygame.draw.rect(self.surf, (220, 220, 220), self.buttonAdd)


        self.playGround = self.surf.get_rect()


    def button(self,x,y,sizeX,sizeY):
        self.buttonRect = pygame.Rect(x, y, sizeX, sizeY)
        return self.buttonRect
