from settings import *
import pygame
import math
import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join(name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Player(pygame.sprite.Sprite):
    image = load_image("assets/player/stand/stand.png")

    def __init__(self):
        super().__init__(ALL_SPRITES, PLAYER_SPRITE)
        self.x, self.y = PLAYER_POS

        self.rect = self.image.get_rect()
        self.rect.x = TILESIZE * 1.5
        self.rect.y = HEIGHT // 2

        self.angle = PLAYER_ANGLE
        self.speed = PLAYER_SPEED

    @property
    def pos(self):
        return self.x, self.y

    def update(self, *args):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.x += self.speed * cos_a
            self.y += self.speed * sin_a
        if keys[pygame.K_s]:
            self.x += -self.speed * cos_a
            self.y += -self.speed * sin_a
        if keys[pygame.K_a]:
            self.x += self.speed * sin_a
            self.y += -self.speed * cos_a
        if keys[pygame.K_d]:
            self.x += -self.speed * sin_a
            self.y += self.speed * cos_a
        if keys[pygame.K_LEFT]:
            self.angle -= 0.05
        if keys[pygame.K_RIGHT]:
            self.angle += 0.05

        self.rect = self.rect.move(self.x, self.y)

