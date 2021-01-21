import math

# параметры игры
WIDTH = 1200
HEIGHT = 800
TILESIZE = 100
FPS = 60

# параметры текстур для разрешения 1200x1200
TEXTURE_WIDTH = 1200
TEXTURE_HEIGHT = 1200
TEXTURE_SCALE = TEXTURE_WIDTH // TILESIZE  # коеффициент масштабирования, чтоб текстура влезла в квадрат стены


# параметры игрока
player_pos = (150, 150)
player_angle = 0
player_speed = 6

# параметры отрисовки
FOV = math.pi / 3
RAYS_NUM = 300
MAX_DEPTH = 800
D_ANGLE = FOV / RAYS_NUM
DISTANCE = RAYS_NUM / (2 * math.tan(FOV / 2))
PROJECTION_COEFF = 3 * DISTANCE * TILESIZE
SCALE = WIDTH // RAYS_NUM

# цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 220, 0)
BLUE = (0, 0, 220)
LIGHTBLUE = (0, 100, 200)
DARKGRAY = (40, 40, 40)
PURPLE = (120, 0, 120)
