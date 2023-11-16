import pygame as pg
from settings import *
vec = pg.math.Vector2


class Sprite():
    def __init__(self, imageclass, x, y):
        self.image = imageclass.image
        # print(id(self.image))
        self.rect = self.image.get_rect()
        self.pos = vec(x * TILESIZE, y * TILESIZE)
        self.rect.topleft = self.pos
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def events(self):
        pass

    def update(self):
        pass


class Wall(Sprite):
    pass


class Block(Sprite):
    pass


class Player(Sprite):

    def events(self):
        self.acc.x, self.acc.y = 0, 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_UP]:
            self.acc.y = -PLAYER_ACC
        if keystate[pg.K_DOWN]:
            self.acc.y = PLAYER_ACC
        if keystate[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keystate[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC

    def update(self):
        # apply friction
        self.acc += self.vel * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        #self.rect.topleft = self.pos


# Hier muss einmal komplett in x und in y Richtung getestet werden. Nicht pro Sprite.
class Collider():

    def collide_with_wall(self, sprite1: Sprite, spritegroup):
        sprite1.rect.x = sprite1.pos.x
        for sprite2 in spritegroup:
            self.collide_with_wall_dir("x", sprite1, sprite2)
        sprite1.rect.y = sprite1.pos.y
        for sprite2 in spritegroup:
            self.collide_with_wall_dir("y", sprite1, sprite2)

    def collide_with_wall_dir(self, dir, sprite1, sprite2):
        if dir == "x":
            if sprite1.rect.colliderect(sprite2.rect):
                if isinstance(sprite2, Wall) or isinstance(sprite2, Block):
                    if sprite1.vel.x >= 0:
                        sprite1.pos.x = sprite2.rect.left - sprite1.rect.width
                    if sprite1.vel.x <= 0:
                        sprite1.pos.x = sprite2.rect.right
                    sprite1.vel.x = 0
                    #sprite1.acc.x = 0
                    sprite1.rect.x = sprite1.pos.x

        if dir == "y":
            if sprite1.rect.colliderect(sprite2.rect):
                if isinstance(sprite2, Wall) or isinstance(sprite2, Block):
                    if sprite1.vel.y >= 0:
                        sprite1.pos.y = sprite2.rect.top - sprite1.rect.height
                    if sprite1.vel.y <= 0:
                        sprite1.pos.y = sprite2.rect.bottom
                    sprite1.vel.y = 0
                    #sprite1.acc.y = 0
                    sprite1.rect.y = sprite1.pos.y
