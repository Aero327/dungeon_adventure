import pygame
import ctypes

# настройки игры
WIDTH = ctypes.windll.user32.GetSystemMetrics(0)
HEIGHT = ctypes.windll.user32.GetSystemMetrics(1)
FPS = 60
TILESIZE = 32
PLAYER_POSITIONS = {
    "player_start": (512, 512),
    "player1": (192, 1726),
    "player2": (1471, 1372),
    "player3": (512, 130),
    "player4": (1788, 481),
    "player5": (2913, 1020)
}

# цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 220, 0)
RED = (220, 0, 0)
BLUE = (0, 0, 220)

# настройки игрока
PLAYER_SPEED = 7

# группы спрайтов
ALL_SPRITES = pygame.sprite.Group()
PLAYER_SPRITE = pygame.sprite.Group()

# остальное
MUSIC_EVENT = pygame.USEREVENT
