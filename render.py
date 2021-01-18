import pygame
from settings import *
from map import world_map


def render(screen, player_pos, player_angle):
    current_angle = player_angle - FOV / 2
    x0, y0 = player_pos
    for ray in range(RAYS_NUM):
        sin_a = math.sin(current_angle)
        cos_a = math.cos(current_angle)
        for d in range(MAX_DEPTH):
            x1 = x0 + d * cos_a
            y1 = y0 + d * sin_a
            if (x1 // TILESIZE * TILESIZE, y1 // TILESIZE * TILESIZE) in world_map and d != 0:
                d *= math.cos(player_angle - current_angle)
                projection_height = PROJECTION_COEFF / d
                c = int(255 / (1 + d * d * 0.00001))
                color = (c, c, c)
                pygame.draw.rect(screen, color, (ray * SCALE, HEIGHT / 2 - projection_height // 2,
                                                 SCALE, projection_height))
                break
        current_angle += D_ANGLE
