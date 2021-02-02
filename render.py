from settings import *
import pygame


class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        info_object = pygame.display.Info()
        self.sizes = (info_object.current_w, info_object.current_h)

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def apply_rect(self, rect):
        return rect.move(self.camera.topleft)

    # updating camera
    def update(self, target):
        player_x, player_y = 0, 0
        x = -target.rect.x + self.sizes[0] / 2  # self.sizes[0] / 2 = 960, допустим x = 1700, x = -740
        y = -target.rect.y + self.sizes[1] / 2  # self.sizes[1] / 2 = 540, допустим y = 1200, y = -660
        print(f"{x}, {y} - камера")

        if x >= 0:
            x = 0
        else:
            player_x = 960
        if y >= 0:
            y = 0
        else:
            player_y = 540
        print(f"{x}, {y} - камера")
        print(f"{player_x}, {player_y} - игрок на камере")

        if x <= -(self.width - self.sizes[0]):  # -(self.width - self.sizes[0]) = -1280
            x = -(self.width - self.sizes[0])  # x = -1280
        else:
            if player_x != 0:
                player_x = 960
        if y <= -(self.height - self.sizes[1]):  # -(self.height - self.sizes[1]) = -936
            y = -(self.height - self.sizes[1])  # y = -936
        else:
            if player_y != 0:
                player_y = 540
        print(f"{x}, {y} - камера")
        print(f"{player_x}, {player_y} - игрок на камере")
        print("-------------------")

        self.camera = pygame.Rect(x, y, self.width, self.height)
        return player_x, player_y
