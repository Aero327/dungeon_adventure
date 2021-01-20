import math

# game settings
WIDTH = 1200
HEIGHT = 800

# player settings
player_pos = (WIDTH // 2 - 100, HEIGHT // 2 - 100)
player_angle = 0
player_speed = 6
FPS = 60
TILESIZE = 100

# render settings
FOV = math.pi / 3
RAYS_NUM = 300
MAX_DEPTH = 1500
D_ANGLE = FOV / RAYS_NUM
DISTANCE = RAYS_NUM / (1.5 * math.tan(FOV / 2))
PROJECTION_COEFF = DISTANCE * TILESIZE
SCALE = WIDTH // RAYS_NUM

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 220, 0)
BLUE = (0, 0, 220)
LIGHTBLUE = (0, 100, 200)
DARKGRAY = (40, 40, 40)
PURPLE = (120, 0, 120)
