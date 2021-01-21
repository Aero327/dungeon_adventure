import pygame
from settings import *
from map import world_map


class Drawing:
    def __init__(self, screen):
        self.screen = screen
        self.texture = pygame.image.load("sprites/wall/2.png").convert()

    def draw_sky_and_floor(self):
        pygame.draw.rect(self.screen, LIGHTBLUE, (0, 0, WIDTH, HEIGHT / 2))
        pygame.draw.rect(self.screen, DARKGRAY, (0, HEIGHT / 2, WIDTH, HEIGHT / 2))

    def world_draw(self, player_pos, player_angle):
        render(self.screen, player_pos, player_angle, self.texture)

    def draw_map(self, player, world_map):
        self.screen.fill((253, 234, 168))
        pygame.draw.line(self.screen, BLACK, player.pos, (player.x + 70 * math.cos(player.angle),
                                                          player.y + 70 * math.sin(player.angle)), 3)
        pygame.draw.circle(self.screen, GREEN, (int(player.x), int(player.y)), 25)
        for x, y in world_map:
            pygame.draw.rect(self.screen, GREEN, (x, y, TILESIZE, TILESIZE), 1)


def current_left_top_of_rect(x, y):
    return (x // TILESIZE) * TILESIZE, (y // TILESIZE) * TILESIZE


def render(screen, player_pos, player_angle, texture):
    # определение начальных параметров
    x0, y0 = player_pos
    cur_rect_x, cur_rect_y = current_left_top_of_rect(x0, y0)
    current_angle = player_angle - FOV / 2

    for ray in range(RAYS_NUM):
        sin_0 = math.sin(current_angle)
        cos_0 = math.cos(current_angle)

        # вертикальное пересечение
        if cos_0 >= 0:
            cur_vertical = cur_rect_x + TILESIZE
            step_vertical = 1
        else:
            cur_vertical = cur_rect_x
            step_vertical = -1

        for i in range(0, WIDTH, TILESIZE):
            d_vertical = (cur_vertical - x0) / cos_0
            cur_horizontal = y0 + d_vertical * sin_0
            if current_left_top_of_rect(cur_vertical + step_vertical, cur_horizontal) in world_map:
                break
            cur_vertical += step_vertical * TILESIZE

        # горизонтальное пересечение
        if sin_0 >= 0:
            cur_horizontal = cur_rect_y + TILESIZE
            step_horizontal = 1
        else:
            cur_horizontal = cur_rect_y
            step_horizontal = -1

        for i in range(0, HEIGHT, TILESIZE):
            d_horizontal = (cur_horizontal - y0) / sin_0
            cur_vertical = x0 + d_horizontal * cos_0
            if current_left_top_of_rect(cur_vertical, cur_horizontal + step_horizontal) in world_map:
                break
            cur_horizontal += step_horizontal * TILESIZE

        # отрисовка
        if d_vertical < d_horizontal:
            d = d_vertical
            offset = cur_horizontal
            offset = int(offset) % TILESIZE
        else:
            d = d_horizontal
            offset = cur_vertical
            offset = int(offset) % TILESIZE

        d *= math.cos(player_angle - current_angle)
        d = max(d, 0.00001)
        projection_height = int(PROJECTION_COEFF / d)
        # делаем подповерхность
        dark_brick_wall = texture.subsurface(offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_HEIGHT)
        dark_brick_wall = pygame.transform.scale(dark_brick_wall, (SCALE, projection_height))  # трансформируем стену под размер прямоугольника, который хотим отрисовать

        screen.blit(dark_brick_wall, (ray * SCALE, HEIGHT // 2 - projection_height // 2))  # наносим текстуру на экран в указанном месте
        # c = 255 / (1 + d ** 2 * 0.00005)
        # color = (c // 10, c, c // 2)
        # pygame.draw.rect(screen, color, (ray * SCALE, HEIGHT // 2 - projection_height // 2, SCALE, projection_height))
        current_angle += D_ANGLE
