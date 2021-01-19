import pygame
from settings import *
from render import render


class Drawing:
    def __init__(self, screen):
        self.screen = screen

    def draw_sky_and_floor(self):
        pygame.draw.rect(self.screen, LIGHTBLUE, (0, 0, WIDTH, HEIGHT / 2))
        pygame.draw.rect(self.screen, DARKGRAY, (0, HEIGHT / 2, WIDTH, HEIGHT / 2))

    def world_draw(self, player_pos, player_angle):
        render(self.screen, player_pos, player_angle)

    def draw_map(self, player, world_map):
        self.screen.fill((253, 234, 168))
        pygame.draw.line(self.screen, BLACK, player.pos, (player.x + 70 * math.cos(player.angle),
                                                          player.y + 70 * math.sin(player.angle)), 3)
        pygame.draw.circle(self.screen, GREEN, (int(player.x), int(player.y)), 25)
        for x, y in world_map:
            pygame.draw.rect(self.screen, GREEN, (x, y, TILESIZE, TILESIZE), 1)
