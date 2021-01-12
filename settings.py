import pygame


WIDTH = 1280  # 32 * 32
HEIGHT = 720  # 32 * 24
SIZE = (WIDTH, HEIGHT)
SCREEN = pygame.display.set_mode(SIZE)
CLOCK = pygame.time.Clock()
FPS = 60

ALL_SPRITES = pygame.sprite.Group()
COLLIDED_TILES_GROUP = pygame.sprite.Group()
NON_COLLIDED_TILES_GROUP = pygame.sprite.Group()
PLAYER_GROUP = pygame.sprite.Group()
