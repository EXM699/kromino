import pygame


class PlayGround(pygame.sprite.Sprite):

    def __init__(self,screenwidth,screenhight):

        super(PlayGround, self).__init__()
        self.rectsize = 26
        self.surf = pygame.Surface((screenwidth,screenhight))

        # Draw the 3 zones
        self.boardTable = pygame.Rect(0, 0, screenwidth - 10, screenhight - 250)
        self.carpet = self.rectImage(0, 0, screenwidth, screenhight, './assets/wall.png', 0,
                                     self.surf)
        #self.score = pygame.Rect(screenwidth - 200, 0, 200, screenhight - 250)
        self.playerTable = pygame.Rect(0, screenhight - 250,screenwidth , 250)

        #self.boardTable = self.rectImage(40, 20, screenwidth - 200, screenhight - 250, './assets/tableFlower.png', 0,
        #                                 self.surf)
        #self.playerTable = self.rectImage(0, screenhight - 250,screenwidth , 250, './assets/table_top.png', 0,
        #                                 self.surf)
        #self.score = self.rectImage(screenwidth - 200, 0, 200, screenhight - 250, './assets/table_top.png', 0,
        #                                 self.surf)
        #iter = screenhight // self.rectsize
        #for i in range(iter - 1):
        #    y = self.rectsize + self.rectsize * i
        #    pygame.draw.line(self.surf,(255,255,255),(0,y),(screenwidth,y))

        #iter = screenwidth // self.rectsize
        #for i in range(iter - 1):
        #    x = self.rectsize + self.rectsize * i
        #    pygame.draw.line(self.surf,(255,255,255),(x,0),(x,screenhight))


        #pygame.draw.rect(self.surf, (255, 0, 0), self.score)
        #pygame.draw.rect(self.surf, (255, 0, 255), self.playerTable)

        arrowCoef = 3
        self.buttonUp = self.rectImage(screenwidth - 300, 5, self.rectsize * arrowCoef, self.rectsize * arrowCoef,
                                    './assets/arrow.png', 90, self.surf)
        self.buttonDown = self.rectImage(screenwidth - 300, 155, self.rectsize * arrowCoef, self.rectsize * arrowCoef,
                                      './assets/arrow.png', -90, self.surf)
        self.buttonLeft = self.rectImage(screenwidth - 375, 80, self.rectsize * arrowCoef, self.rectsize * arrowCoef,
                                      './assets/arrow.png', 180, self.surf)
        self.buttonRight = self.rectImage(screenwidth - 225, 80, self.rectsize * arrowCoef, self.rectsize * arrowCoef,
                                       './assets/arrow.png', 0, self.surf)
        self.buttonAdd = self.rectImage(screenwidth - 300, 80, self.rectsize * arrowCoef, self.rectsize * arrowCoef,
                                     './assets/bag2.png', 0, self.surf)

        self.playGround = self.surf.get_rect()


    def rectImage(self, x, y, sizeX, sizeY, icon, angle, surface):
        coefRot = float(angle)
        self.rect = pygame.Rect(x, y, sizeX, sizeY)

        #self.rect = pygame.Rect(x, y, sizeX, sizeY)
        self.icon = pygame.image.load(icon)
        self.icon = pygame.transform.scale(self.icon, (sizeX, sizeY))

        self.icon = pygame.transform.rotate(self.icon, coefRot)

        surface.blit(self.icon, self.rect)
        #pygame.display.flip()

        return self.rect

    def score(self,Score=0):
        tenPart = int(Score / 10)
        unitPart = Score % 10

        fileTen = './assets/' + str(tenPart) + '.png'
        fileUnit = './assets/' + str(unitPart) + '.png'
        numberL = pygame.image.load(fileTen)
        numberR = pygame.image.load(fileUnit)

        numberL = pygame.transform.scale(numberL, (40, 40))
        numberR = pygame.transform.scale(numberR, (40, 40))

        return (numberL, numberR)


    def scoreBoard(self, result, x, y,message ):


        splitResult = self.score(result)

        rect = pygame.Rect(x, y, 200, 100)

        computerRectL = pygame.Rect(x+65, y+33, 30, 30)
        computerRectR = pygame.Rect(x+95, y+33, 30, 30)

        scoreBoard = pygame.image.load('./assets/score_board2.png')
        scoreBoard = pygame.transform.scale(scoreBoard, (200, 100))

        font = pygame.font.SysFont(None, 24)
        img = font.render(message, True, (0,0,0))

        self.surf.blit(scoreBoard, rect)
        self.surf.blit(splitResult[0], computerRectL)
        self.surf.blit(splitResult[1], computerRectR)
        mX = int ((200 - len(message)) / 4)

        if mX < 0:
            mX = x + 5
        else:
            mX = mX + x


        #mX = x + 20
        mY = y + 20

        self.surf.blit(img, (mX, mY))

