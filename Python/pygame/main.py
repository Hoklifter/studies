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
playerX_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

# Game Loop
running = True
while running:

    # RBG - Red, Green, Blue
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check wheter its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
                print(f'{playerX_change = }')
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
                print(f'{playerX_change = }')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                print(f'{playerX_change = }')


    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= WIDTH - 64:
        playerX = WIDTH - 64
    player(playerX, playerY)
    pygame.display.update()
