from settings import *
import pygame


class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        info_object = pygame.display.Info()
        self.sizes = (info_object.current_w, info_object.current_h)

        self.player_at_left_side = False
        self.player_at_top_side = False
        self.player_at_bottom_side = False
        self.player_at_right_side = False

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def apply_rect(self, rect):
        return rect.move(self.camera.topleft)

    # updating camera
    def update(self, target):
        self.player_at_left_side = False
        self.player_at_top_side = False
        self.player_at_bottom_side = False
        self.player_at_right_side = False

        player_x, player_y = 0, 0
        x = -target.rect.x + self.sizes[0] / 2
        y = -target.rect.y + self.sizes[1] / 2

        if x >= 0:
            x = 0
            player_x = 0
            self.player_at_left_side = True
        else:
            player_x = 960
        if y >= 0:
            y = 0
            player_y = 0
            self.player_at_top_side = True
        else:
            player_y = 540
        print(f"{x}, {y} - камера")
        print(f"{player_x}, {player_y} - игрок на камере")

        if x <= -(self.width - self.sizes[0]):  # -(self.width - self.sizes[0]) = -1280
            x = -(self.width - self.sizes[0])  # x = -1280
            player_x = 0
            self.player_at_right_side = True
        else:
            if not self.player_at_left_side:
                player_x = 960
        if y <= -(self.height - self.sizes[1]):  # -(self.height - self.sizes[1]) = -936
            y = -(self.height - self.sizes[1])  # y = -936
            player_y = 0
            self.player_at_bottom_side = True
        else:
            if not self.player_at_top_side:
                player_y = 540
        print(f"{x}, {y} - камера")
        print(f"{player_x}, {player_y} - игрок на камере")

        self.camera = pygame.Rect(x, y, self.width, self.height)

        return player_x, player_y
