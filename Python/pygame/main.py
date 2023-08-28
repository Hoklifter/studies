import pygame

# Initialize the pygame
pygame.init()

# Create the screen
WIDTH = 400
HEIGHT = 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ship32.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('ship64.png')
playerX = WIDTH // 2 - 32
playerY = (HEIGHT // 3) * 2

def player():
    screen.blit(playerImg, (playerX, playerY))

# Game Loop
running = True
while running:

    # RBG - Red, Green, Blue
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((0, 0, 0))
    player()
    pygame.display.update()
