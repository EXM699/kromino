import pygame

class PlayGround(pygame.sprite.Sprite):
    def __init__(self,screenwidth,screenhight):

        super(PlayGround, self).__init__()
        self.rectsize = 27
        self.surf = pygame.Surface((screenwidth,screenhight))

        # Draw the 3 zones
        self.boardTable = pygame.Rect(0, 0, screenwidth - 200, screenhight - 250)
        self.score = pygame.Rect(screenwidth - 200, 0, 200, screenhight - 250)
        self.playerTable = pygame.Rect(0, screenhight - 250,screenwidth , 250)

        self.buttonUp = self.button(screenwidth - 300, screenhight - 400)
        self.buttonDown = self.button(screenwidth - 300, screenhight - 350)
        self.buttonLeft = self.button(screenwidth - 350, screenhight - 375)
        self.buttonRight = self.button(screenwidth - 250, screenhight - 375)

        pygame.draw.rect(self.surf, (255,255,0), self.boardTable)


        #iter = screenhight // self.rectsize
        #for i in range(iter - 1):
        #    y= self.rectsize + self.rectsize * i
        #    pygame.draw.line(self.surf,(255,0,0),(0,y),(screenwidth,y))

        pygame.draw.rect(self.surf, (255, 0, 0), self.score)
        pygame.draw.rect(self.surf, (0, 0, 255), self.playerTable)

        pygame.draw.rect(self.surf, (220, 220, 220), self.buttonUp)
        pygame.draw.rect(self.surf, (220, 220, 220), self.buttonLeft)
        pygame.draw.rect(self.surf, (220, 220, 220), self.buttonRight)
        pygame.draw.rect(self.surf, (220, 220, 220), self.buttonDown)

        self.playGround = self.surf.get_rect()


    def button(self,x,y):
        self.buttonRect = pygame.Rect(x, y, self.rectsize, self.rectsize)
        return self.buttonRect
