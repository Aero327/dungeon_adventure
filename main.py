import pygame
from settings import *
from player import Player
from map import world_map
from render import render
import math

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    player.movement()
    screen.fill(BLACK)

    pygame.draw.rect(screen, LIGHTBLUE, (0, 0, WIDTH, HEIGHT / 2))
    pygame.draw.rect(screen, DARKGRAY, (0, HEIGHT / 2, WIDTH, HEIGHT / 2))

    render(screen, player.pos, player.angle)

    # pygame.draw.circle(screen, GREEN, (int(player.x), int(player.y)), 25)
    # pygame.draw.line(screen, GREEN, player.pos, (player.x + WIDTH * math.cos(player.angle),
    #                                             player.y + WIDTH * math.sin(player.angle)))
    # for x, y in world_map:
    #    pygame.draw.rect(screen, DARKGRAY, (x, y, TILESIZE, TILESIZE), 5)

    pygame.display.flip()
    clock.tick(FPS)
