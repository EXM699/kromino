import pygame


class PlayGround(pygame.sprite.Sprite):

    def __init__(self,screenwidth,screenhight):

        super(PlayGround, self).__init__()
        self.rectsize = 26
        self.surf = pygame.Surface((screenwidth,screenhight))

        # Draw the 3 zones
        self.boardTable = pygame.Rect(0, 0, screenwidth - 200, screenhight - 250)
        self.carpet = self.rectImage(0, 0, screenwidth, screenhight, './assets/wall2.png', 0,
                                     self.surf)
        self.score = pygame.Rect(screenwidth - 200, 0, 200, screenhight - 250)
        self.playerTable = pygame.Rect(0, screenhight - 250,screenwidth , 250)
        #self.boardTable = self.rectImage(40, 20, screenwidth - 200, screenhight - 250, './assets/tableFlower.png', 0,
        #                                 self.surf)
        #self.playerTable = self.rectImage(0, screenhight - 250,screenwidth , 250, './assets/table_top.png', 0,
        #                                 self.surf)
        #self.score = self.rectImage(screenwidth - 200, 0, 200, screenhight - 250, './assets/table_top.png', 0,
        #                                 self.surf)
        iter = screenhight // self.rectsize
        #for i in range(iter - 1):
        #    y = self.rectsize + self.rectsize * i
        #    pygame.draw.line(self.surf,(255,255,255),(0,y),(screenwidth,y))


        iter = screenwidth // self.rectsize
        #for i in range(iter - 1):
        #    x = self.rectsize + self.rectsize * i
        #    pygame.draw.line(self.surf,(255,255,255),(x,0),(x,screenhight))


        #pygame.draw.rect(self.surf, (255, 0, 0), self.score)
        #pygame.draw.rect(self.surf, (255, 0, 255), self.playerTable)

        self.buttonUp = self.rectImage(screenwidth - 300, screenhight - 400, self.rectsize, self.rectsize,
                                    './assets/arrow_right.png', 90, self.surf)
        self.buttonDown = self.rectImage(screenwidth - 300, screenhight - 350, self.rectsize, self.rectsize,
                                      './assets/arrow_right.png', -90, self.surf)
        self.buttonLeft = self.rectImage(screenwidth - 350, screenhight - 375, self.rectsize, self.rectsize,
                                      './assets/arrow_right.png', 180, self.surf)
        self.buttonRight = self.rectImage(screenwidth - 250, screenhight - 375, self.rectsize, self.rectsize,
                                       './assets/arrow_right.png', 0, self.surf)
        self.buttonAdd = self.rectImage(screenwidth - 100, screenhight - 375, self.rectsize * 3, self.rectsize * 3,
                                     './assets/button_add.png', 0, self.surf)

        self.playGround = self.surf.get_rect()


    def rectImage(self, x, y, sizeX, sizeY, icon, angle, surface):
        coefRot = float(angle)
        self.rect = pygame.Rect(x, y, sizeX, sizeY)

        #self.rect = pygame.Rect(x, y, sizeX, sizeY)
        self.icon = pygame.image.load(icon)
        self.icon = pygame.transform.scale(self.icon, (sizeX, sizeY))

        self.icon = pygame.transform.rotate(self.icon, coefRot)

        surface.blit(self.icon, self.rect)

        return self.rect
