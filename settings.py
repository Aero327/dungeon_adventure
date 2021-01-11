import pygame
import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('images', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


SIZE = WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode(SIZE)
CLOCK = pygame.time.Clock()
FPS = 60

ALL_SPRITES = pygame.sprite.Group()
TILES_GROUP = pygame.sprite.Group()
PLAYER_GROUP = pygame.sprite.Group()

TILE_WIDTH = TILE_HEIGHT = 25
TILE_IMAGES = {
    "floor": load_image('floor.png')
}

PLAYER_IMAGES = {
    "standing": load_image("knight.png")
}
