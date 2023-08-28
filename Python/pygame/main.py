import pygame

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((400, 300))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RBG - Red, Green, Blue
    screen.fill((255, 0, 0))
    pygame.display.update()
