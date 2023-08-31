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
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('alien64.png'))
    enemyX.append(random.randint(0, WIDTH-64))
    enemyY.append(random.randint(0, (HEIGHT // 2)-64))
    enemyX_change.append(0.3)
    enemyY_change.append(40)


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

# Bullet

# Ready - You can't see the bullet on the screen
# Fire  - The bullet is currently moving

bulletImg = pygame.image.load('bullet32.png')
bulletX = 0
bulletY = playerY
bulletY_change = 10
bullet_state = 'ready'
# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

def show_score(x, y):
    score = font.render(f"Score: {score_value}", True, (255, 255, 255))
    screen.blit(score, (x, y))

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


    # Enemy Movement
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= WIDTH - 64:
            enemyX_change[i] = -0.5
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = playerY
            bullet_state = 'ready'
            score_value += 1

            enemyX[i] = random.randint(0, WIDTH-64)
            enemyY[i] = random.randint(0, (HEIGHT // 2)-64)

        enemy(enemyX[i], enemyY[i], i)
    # Bullet Movement
    if bulletY <= 0:
        bulletY = playerY
        bullet_state = 'ready'

    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
