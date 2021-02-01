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
        x = 0 + -(target.rect.x - self.sizes[0] // 2)
        y = 0 + -(target.rect.y - self.sizes[1] // 2)

        x = min(0, x)
        y = min(0, y)

        x = max(-(self.width - self.sizes[0]), x)
        y = max(-(self.height - self.sizes[1]), y)

        self.camera = pygame.Rect(x, y, self.width, self.height)
        print(x, y)
