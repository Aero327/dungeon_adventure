from settings import *
import pygame
import math


class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle
        self.speed = player_speed

    @property
    def pos(self):
        return self.x, self.y

    def movement(self):
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
            self.x += self.speed * cos_a
            self.y += -self.speed * sin_a
        if keys[pygame.K_d]:
            self.x += -self.speed * cos_a
            self.y += self.speed * sin_a
        if keys[pygame.K_LEFT]:
            self.angle -= 0.05
        if keys[pygame.K_RIGHT]:
            self.angle += 0.05
