import pygame
import ctypes

# настройки игры
WIDTH = ctypes.windll.user32.GetSystemMetrics(0)
HEIGHT = ctypes.windll.user32.GetSystemMetrics(1)
FPS = 60
TILESIZE = 32

# цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 220, 0)
RED = (220, 0, 0)

# настройки игрока
PLAYER_SPEED = 2

# группы спрайтов
ALL_SPRITES = pygame.sprite.Group()
PLAYER_SPRITE = pygame.sprite.Group()

# остальное
MUSIC_EVENT = pygame.USEREVENT
