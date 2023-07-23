# Import the pygame module
import pygame
from pygame import draw, sprite
from pygame.draw import rect

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP,
    MOUSEMOTION,
)


# Define constants for the screen width and height

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'

class Player(pygame.sprite.Sprite):
    #def __init__(self):
    #    lenRect = (25,25)
    #    super(Player, self).__init__()
    #    self.surf = pygame.Surface(lenRect)
    #    self.surf.fill((255, 255, 255))
    #    self.rect = self.surf.get_rect()
    #    self.focus = False

    def __init__(self):
        super(Player, self).__init__()
        square_size = 25
        margin = 0
        lenBlock = ((square_size+margin)*3,square_size)
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

        self.rect = self.surf.get_rect()
        self.focus = False

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

    # Move the sprite based on mouse motion
    def motionByMouse(self, rel):
        self.rect.move_ip(event.rel)


# Initialize pygame

pygame.init()


# Create the screen object

# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Instantiate player. Right now, this is just a rectangle.
player = Player()

# Variable to keep the main loop running

running = True

clock = pygame.time.Clock()

# Main loop
while running:
    # for loop through the event queue
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == MOUSEBUTTONDOWN and player.rect.collidepoint(mouse_pos):
            #print('mouse down')
            player.focus = True
        elif event.type == MOUSEBUTTONUP:
            player.focus = False
        elif event.type == MOUSEMOTION and player.focus:
            player.motionByMouse(event.rel)

        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False
        # Get all the keys currently pressed

    pressed_keys = pygame.key.get_pressed()


    # Update the player sprite based on user keypresses

    player.update(pressed_keys)

    # Fill the screen with black
    screen.fill((0, 0, 0))


    # Draw the player on the screen
    #screen.blit(player.surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    screen.blit(player.surf, player.rect)

    # Update the display
    pygame.display.flip()

    clock.tick(30)