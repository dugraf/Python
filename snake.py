import pygame, random
from pygame.locals import *

def onGridRandom():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10 * 10, y//10 * 10)

def wallColision(n, m):
    if (n == m):
        return True

def collision(c1, c2):
    return (c1[0] == c2[0] and (c1[1] == c2[1]))

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('COBRINHA')

snake = [(200, 200), (210, 200), (220, 200)]
snakeSkin = pygame.Surface((10, 10))
snakeSkin.fill((255, 255, 255))

apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))
applePos = onGridRandom()

wall = [(200, 200), (210, 200), (220, 200)]
wallSkin = pygame.Surface((50,10))
wallSkin.fill((0, 0, 255))
wallPos = onGridRandom()

myDirection = LEFT

font = pygame.font.Font('poppins.ttf')
score = 0

clock = pygame.time.Clock()

game_over = False

while not game_over:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                myDirection = UP

            if event.key == K_DOWN:
                myDirection = DOWN

            if event.key == K_LEFT:
                myDirection = LEFT

            if event.key == K_RIGHT:
                myDirection = RIGHT

    if collision(snake[0], applePos):
        applePos = onGridRandom()
        snake.append((0,0))

    if wallColision(snake[0], wall):
        pygame.quit()

    if myDirection == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    
    if myDirection == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)

    if myDirection == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])

    if myDirection == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake [i - 1][0], snake [i - 1][1])

    screen.fill((0, 0, 0))
    screen.blit(apple, applePos)
    screen.blit(wallSkin, wallPos)

    for pos in snake:
        screen.blit(snakeSkin, pos)

    pygame.display.update()