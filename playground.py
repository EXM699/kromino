import pygame

class PlayGround(pygame.sprite.Sprite):
    def __init__(self,screenwidth,screenhight):

        super(PlayGround, self).__init__()
        self.surf = pygame.Surface((screenwidth,screenhight))

        # Draw the 3 zones
        self.boardTable = pygame.Rect(0, 0, screenwidth - 200, screenhight - 250)
        self.score = pygame.Rect(screenwidth - 200, 0, 200, screenhight - 250)
        self.playerTable = pygame.Rect(0, screenhight - 250,screenwidth , 250)

        pygame.draw.rect(self.surf, (255,255,0), self.boardTable)
        pygame.draw.rect(self.surf, (255, 0, 0), self.score)
        pygame.draw.rect(self.surf, (0, 0, 255), self.playerTable)

        self.playGround = self.surf.get_rect()


