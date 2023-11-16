
import pygame
import os
from settings import *
import random
from abc import ABC, abstractmethod


class Sprite(ABC):
    @abstractmethod
    def update():
        pass


class Ball(Sprite):
    def __init__(self, x, y, vx, vy, image_dict):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        game_folder = os.path.dirname(__file__)
        self.image = image_dict["ball"]
        self.imageRect = self.image.get_rect()
        print(id(self.image))

    def update(self):

        # Kollision am Rand
        if self.imageRect.right >= WIDTH or self.imageRect.left <= 0:
            self.vx = self.vx * -1
        if self.imageRect.bottom >= HEIGHT or self.imageRect.top <= 0:
            self.vy = self.vy * -1

        # Bewegungsgleichung
        self.x = self.x + self.vx
        self.y = self.y + self.vy

        # Aktualsierung
        self.imageRect.topleft = (self.x, self.y)


class Coin(Sprite):
    def __init__(self, x, y, vx, vy, image_dict):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.image_dict = image_dict

        # Animation
        self.max_frames = 8
        self.akt_frame = random.randint(1, 8)
        self.anim_rate = 4
        self.image = self.image_dict["coin"+str(self.akt_frame)]
        self.imageRect = self.image.get_rect()
        self.timer = 0

    def update(self):

        # Animation
        self.timer += 1
        if self.timer > self.anim_rate:
            self.timer = 0
            self.akt_frame += 1
            if self.akt_frame > self.max_frames:
                self.akt_frame = 1
                #self.timer = 0
            self.image = self.image_dict["coin"+str(self.akt_frame)]

        # Kollision am Rand
        if self.imageRect.right >= WIDTH or self.imageRect.left <= 0:
            self.vx = self.vx * -1
        if self.imageRect.bottom >= HEIGHT or self.imageRect.top <= 0:
            self.vy = self.vy * -1

        # Bewegungsgleichung
        self.x = self.x + self.vx
        self.y = self.y + self.vy

        # Aktualsierung
        self.imageRect.topleft = (self.x, self.y)
