import pygame
from settings import *
from map import world_map


def current_left_top_of_rect(x, y):
    return (x // TILESIZE) * TILESIZE, (y // TILESIZE) * TILESIZE


def render(screen, player_pos, player_angle):
    # определение начальных параметров
    x0, y0 = player_pos
    cur_rect_x, cur_rect_y = current_left_top_of_rect(x0, y0)
    current_angle = player_angle - FOV / 2

    for ray in range(RAYS_NUM):
        sin_0 = math.sin(current_angle)
        cos_0 = math.cos(current_angle)

        # вертикальное пересечение
        if cos_0 >= 0:
            cur_vertical, step_vertical = (cur_rect_x + TILESIZE, 1)
        else:
            cur_vertical, step_vertical = (cur_rect_x, -1)

        for i in range(0, WIDTH, TILESIZE):
            d_vertical = (cur_vertical - x0) / cos_0
            cur_horizontal = y0 + d_vertical * sin_0
            if current_left_top_of_rect(cur_vertical + step_vertical, cur_horizontal) in world_map:
                break
            cur_vertical += step_vertical * TILESIZE

        # горизонтальное пересечение
        if sin_0 >= 0:
            cur_horizontal, step_horizontal = (cur_rect_y + TILESIZE, 1)
        else:
            cur_horizontal, step_horizontal = (cur_rect_y, -1)

        for i in range(0, HEIGHT, TILESIZE):
            d_horizontal = (cur_horizontal - y0) / sin_0
            cur_vertical = x0 + d_horizontal * cos_0
            if current_left_top_of_rect(cur_vertical, cur_horizontal + step_horizontal) in world_map:
                break
            cur_horizontal += step_horizontal * TILESIZE

        # отрисовка
        if d_vertical < d_horizontal:
            d = d_vertical
        else:
            d = d_horizontal

        d *= math.cos(player_angle - current_angle)
        d = max(d, 0.00001)
        projection_height = PROJECTION_COEFF / d
        c = 255 / (1 + d ** 2 * 0.00005)
        color = (c // 10, c, c // 2)
        pygame.draw.rect(screen, color, (ray * SCALE, HEIGHT // 2 - projection_height // 2, SCALE, projection_height))
        current_angle += D_ANGLE
