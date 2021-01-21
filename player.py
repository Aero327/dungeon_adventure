from settings import *
import pygame
import math


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(ALL_SPRITES, PLAYER_SPRITE)
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.speed = PLAYER_SPEED

    @property
    def pos(self):
        return self.x, self.y

    def movement(self, level_map):
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
