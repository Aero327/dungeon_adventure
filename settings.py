import pygame

# настройки игры
WIDTH = 1280
HEIGHT = 720
FPS = 60
TILESIZE = 40  # 32 клеток по 40 пикселей в ширину, 18 клеток по 40 пикселей в высоту

# цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 220, 0)
RED = (220, 0, 0)

# настройки игрока
PLAYER_POS = (TILESIZE * 1.5, HEIGHT // 2)
PLAYER_ANGLE = 0
PLAYER_SPEED = 3

# группы спрайтов
ALL_SPRITES = pygame.sprite.Group()
PLAYER_SPRITE = pygame.sprite.Group()
WALL_SPRITES = pygame.sprite.Group()
