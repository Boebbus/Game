#!/usr/bin/python
import pygame
import os
from abc import ABC, abstractmethod
import random

WIDTH = 400
HEIGHT = 600

pygame.init()
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bruch')

# Game Folder
game_folder = os.path.dirname(__file__)

# Hintergrund = pygame.image.load(game_folder + '/images\Galaxy.jpg')

DARKBLUE = (0, 0, 0.2)

# bat init
bat = pygame.image.load(game_folder + '/images/bat.png')
playerY = HEIGHT - 50
batRect = bat.get_rect()
mousex, mousey = (0, playerY)

# ball init
ball = pygame.image.load(game_folder + '/images/ball.png')
ballRect = ball.get_rect()
ballStartY = 300
ballSpeed = 3
ballServed = False
bx, by = (24, ballStartY)
sx, sy = (ballSpeed, ballSpeed)
ballRect.topleft = (bx, by)

# brick init

brick = None
bricks = []

# class Objekt(ABC):
#     @abstractmethod
#     def use(self):
#         pass

class BrickNormal:
    BrickNormal = pygame.image.load(game_folder + '/images/brick.png')
    Chance = 95
    # def __init__(self, img):
    #     self.img = img

class BrickPowerUp:
    BrickPowerUp = pygame.image.load(game_folder + '/images/brickPowerUp.png')
    Chance = 5

def BrickFactory(rows):
    for y in range(rows):

        if random.randint(0,95) <= BrickNormal.Chance:
            global brick
            brick = pygame.image.load(game_folder + '/images/brick.png')
            width = brick.get_width()
            height = brick.get_height()
            print(f"{height} {width} {brick}")
            rect = pygame.Rect(width, height)

            bricks.append(rect)


# def createBricks(cols, rows):
#     global brick
#     brick = pygame.image.load(game_folder + '/images/brickPowerUp.png')
#     for y in range(rows):
#         brickY = (y * 24) + 100
#         for x in range(cols):
#             brickX = (x * 31) + 50
#             RectWidth = brick.get_width()
#             RectHeight = brick.get_height()
#             rect = pygame.Rect(brickX, brickY, RectWidth, RectHeight)
#             bricks.append(rect)

# createBricks(10, 5)
BrickFactory(5)
print(bricks)

running = True

while running:
    screen.fill(DARKBLUE)
    # brick draw
    # for b in bricks:
    #     screen.blit(brick, b)

    # bat and ball draw
    screen.blit(bat, batRect)
    screen.blit(ball, ballRect)

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            mousex, mousey = event.pos
            if (mousex < WIDTH - 55):
                batRect.topleft = (mousex, playerY)
            else:
                batRect.topleft = (WIDTH - 55, playerY)
        elif event.type == pygame.MOUSEBUTTONUP and not ballServed:
            ballServed = True

    # main game logic

    if ballServed:
        bx += sx
        by += sy
        ballRect.topleft = (bx, by)

    if (by <= 0):
        by = 0
        sy *= -1

    if (by >= HEIGHT - 8):
        by = HEIGHT - 8
        sy *= -1

    if (bx <= 0):
        bx = 0
        sx *= -1

    if (bx >= WIDTH - 8):
        bx = WIDTH - 8
        sx *= -1

    if (by >= HEIGHT - 8):
        ballServed = False
        bx, by = (24, ballStartY)
        ballSpeed = 3
        sx, sy = (ballSpeed, ballSpeed)
        ballRect.topleft = (bx, by)

    # collision detection
    brickHitIndex = ballRect.collidelist(bricks)
    if brickHitIndex >= 0:
        hb = bricks[brickHitIndex]
        mx = bx + 4
        my = by + 4
        if mx > hb.x + hb.width or mx < hb.x:
            sx *= -1
        else:
            sy *= -1
        del (bricks[brickHitIndex])

    # ball bast collision
    if ballRect.colliderect(batRect):
        by = playerY - 8
        sy *= -1

    pygame.display.update()
    dt = fpsClock.tick(60)

if len(bricks) == 0:
    running = False

pygame.quit()
