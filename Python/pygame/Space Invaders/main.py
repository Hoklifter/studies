import pygame
import random
import math

# Initialize the pygame
pygame.init()

# Create the screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Background
background = pygame.image.load('background.jpg')

# Caption and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ship32.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('ship64.png')
playerX = WIDTH // 2 - 32
playerY = HEIGHT - 64 - 10
playerX_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

# Enemy
enemyImg = pygame.image.load('alien64.png')
enemyX = random.randint(0, WIDTH-64)
enemyY = random.randint(0, (HEIGHT // 2)-64)
enemyX_change = 0.3
enemyY_change = 40

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

# Bullet

# Ready - You can't see the bullet on the screen
# Fire  - The bullet is currently moving

bulletImg = pygame.image.load('bullet32.png')
bulletX = 0
bulletY = playerY
bulletY_change = 10
bullet_state = 'ready'

score = 0

def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance =  math.sqrt(
        (enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2
    )
    if distance < 27:
        return True
    return False

# Game Loop
running = True
while running:

    # RBG - Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check wheter its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1

            if event.key == pygame.K_RIGHT:
                playerX_change = 1

            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    # Get current x coordinate of the player
                    bulletX = playerX
                    bullet_state = 'fire'

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


    # Boundaries control
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= WIDTH - 64:
        playerX = WIDTH - 64

    enemyX += enemyX_change

    # Enemy Movement
    if enemyX <= 0:
        enemyX_change = 0.5
        enemyY += enemyY_change
    elif enemyX >= WIDTH - 64:
        enemyX_change = -0.5
        enemyY += enemyY_change

    # Bullet Movement
    if bulletY <= 0:
        bulletY = playerY
        bullet_state = 'ready'

    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Collision
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = playerY
        bullet_state = 'ready'
        score += 1
        print(score)
        enemyX = random.randint(0, WIDTH-64)
        enemyY = random.randint(0, (HEIGHT // 2)-64)

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
