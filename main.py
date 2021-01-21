import pygame
from settings import *
from player import Player
from render import *
from map import world_map

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dungeon Adventures")
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(screen)
map_drawing = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                print(map_drawing)
                map_drawing = -map_drawing

    player.movement()
    screen.fill(BLACK)

    drawing.draw_sky_and_floor()
    drawing.world_draw(player.pos, player.angle)
    if map_drawing == -1:
        drawing.draw_map(player, world_map)

    pygame.display.flip()
    clock.tick(FPS)
