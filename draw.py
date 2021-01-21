import pygame
import math
from settings import *


class Drawing:
    def __init__(self, screen):
        self.screen = screen

    def draw_map(self, player, level_map):
        self.screen.fill(BLACK)
        pygame.draw.line(self.screen, WHITE, player.pos, (player.x + 30 * math.cos(player.angle),
                                                          player.y + 30 * math.sin(player.angle)), 3)
        pygame.draw.circle(self.screen, RED, (int(player.x), int(player.y)), 10)
        for x, y in level_map:
            pygame.draw.rect(self.screen, GREEN, (x, y, TILESIZE, TILESIZE))
