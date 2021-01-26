import pygame
import sys
from settings import *
from map import level1_map
from draw import Drawing
from player import Player


class Wall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(ALL_SPRITES, WALL_SPRITES)


def terminate():
    pygame.quit()
    sys.exit()


def start_screen(screen, clock):
    font = pygame.font.Font(None, 80)
    text = ("Agent 007", "",
            "Press any key to continue")
    text_coord = 30
    for line in text:
        string_rendered = font.render(line, 1, WHITE)
        intro_rect = string_rendered.get_rect()
        text_coord += 100
        intro_rect.top = text_coord
        intro_rect.x = WIDTH // 2 - intro_rect.w // 2
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return False
            if ev.type == pygame.KEYDOWN or ev.type == pygame.MOUSEBUTTONDOWN:
                return True

        pygame.display.flip()
        clock.tick(FPS)


def start():
    pygame.init()
    if not start_screen(screen, clock):
        terminate()
    return True


if __name__ == "__main__":
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Agent 007")
    clock = pygame.time.Clock()

    start()

    while True:
        player = Player()
        drawing = Drawing(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

        screen.fill(BLACK)

        drawing.draw_map(level1_map)

        ALL_SPRITES.draw(screen)
        ALL_SPRITES.update()

        pygame.display.flip()
        clock.tick(FPS)
