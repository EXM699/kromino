import pygame
from pygame import event


class Blocks(pygame.sprite.Sprite):
    def __init__(self):
        super(Blocks, self).__init__()
        square_size = 25
        margin = 0
        lenBlock = ((square_size + margin) * 3, square_size)
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 255)
        self.surf = pygame.Surface(lenBlock)

        # Dessiner les rectangles
        rect1 = pygame.Rect(margin, margin, square_size, square_size)
        rect2 = pygame.Rect(margin + square_size + margin, margin, square_size, square_size)
        rect3 = pygame.Rect(margin + (square_size + margin) * 2, margin, square_size, square_size)

        # Dessiner les rectangles sur l'écran
        pygame.draw.rect(self.surf, RED, rect1)  # Rouge
        pygame.draw.rect(self.surf, BLUE, rect2)  # Bleu
        pygame.draw.rect(self.surf, GREEN, rect3)  # Vert

        self.block = self.surf.get_rect()
        self.focus = False


    # Move the sprite based on mouse motion
    def motionByMouse(self, rel):
        self.block.move_ip(rel)
