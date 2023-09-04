import pygame

class Button:
    def __init__(self, x, y, width, height, icon, orientation,surface):
        self.rect = pygame.Rect(x, y, width, height)
        self.icon = pygame.image.load(icon)
        self.icon = pygame.transform.scale(self.icon, (width, height))
        if orientation == 'UP':
            self.icon = pygame.transform.rotate(self.icon, 90)

        surface.blit(self.icon, self.rect)

    def draw(self, surface):
        surface.blit(self.icon, self.rect)
        #print(surface)

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



        #self.buttonUp = self.button(screenwidth - 300, screenhight - 400,self.rectsize,self.rectsize)
        #self.buttonDown = self.button(screenwidth - 300, screenhight - 350,self.rectsize,self.rectsize)
        #self.buttonLeft = self.button(screenwidth - 350, screenhight - 375,self.rectsize,self.rectsize)
        #self.buttonRight = self.button(screenwidth - 250, screenhight - 375,self.rectsize,self.rectsize)
        #self.buttonAdd = self.button(screenwidth - 100, screenhight - 375,self.rectsize * 3,self.rectsize * 3)


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

        #pygame.draw.rect(self.surf, (220, 220, 220), self.buttonUp)
        #pygame.draw.rect(self.surf, (220, 220, 220), self.buttonLeft)
        #pygame.draw.rect(self.surf, (220, 220, 220), self.buttonRight)
        #pygame.draw.rect(self.surf, (220, 220, 220), self.buttonDown)
        #pygame.draw.rect(self.surf, (220, 220, 220), self.buttonAdd)

        #self.myButton = Button(screenwidth - 300, screenhight - 400, self.rectsize, self.rectsize,
        #                       './assets/arrow_right.png','UP',self.surf)

        self.buttonUp = self.button(screenwidth - 300, screenhight - 400, self.rectsize, self.rectsize,
                                    './assets/arrow_right.png', 'UP', self.surf)
        self.buttonDown = self.button(screenwidth - 300, screenhight - 350, self.rectsize, self.rectsize,
                                      './assets/arrow_right.png', 'DOWN', self.surf)
        self.buttonLeft = self.button(screenwidth - 350, screenhight - 375, self.rectsize, self.rectsize,
                                      './assets/arrow_right.png', 'LEFT', self.surf)
        self.buttonRight = self.button(screenwidth - 250, screenhight - 375, self.rectsize, self.rectsize,
                                       './assets/arrow_right.png', 'RIGHT', self.surf)
        self.buttonAdd = self.button(screenwidth - 100, screenhight - 375, self.rectsize * 3, self.rectsize * 3,
                                     './assets/arrow_right.png', 'ADD', self.surf)

        self.playGround = self.surf.get_rect()


    def button(self,x,y,sizeX,sizeY,icon,orientation,surface ):
        coefRot = 0
        self.rect = pygame.Rect(x, y, sizeX, sizeY)

        #self.rect = pygame.Rect(x, y, sizeX, sizeY)
        self.icon = pygame.image.load(icon)
        self.icon = pygame.transform.scale(self.icon, (sizeX, sizeY))

        if orientation == 'UP':
            coefRot = 90
        elif orientation == 'RIGHT':
            coefRot = 0
        elif orientation == 'DOWN':
            coefRot = -90
        elif orientation == 'LEFT':
            coefRot = 180

        self.icon = pygame.transform.rotate(self.icon, coefRot)

        surface.blit(self.icon, self.rect)

        return self.rect
