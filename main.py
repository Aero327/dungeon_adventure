import pygame
import sys
from random import randint
from os import path
from settings import *
from player import load_image, Player
from render import Camera
from map import Map


def terminate():
    pygame.quit()
    sys.exit()


def start_screen(screen, clock):
    background = load_image("assets/map icons/background.png")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    font_name = path.join("assets/font", "18177.otf")
    font = pygame.font.Font(font_name, 80)
    text = ("Neverland", "",
            "Press any key to continue")
    text_coord = 30
    screen.blit(background, (0, 0))
    for line in text:
        string_rendered = font.render(line, 1, BLACK)
        intro_rect = string_rendered.get_rect()
        text_coord += 90
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


def init_music():
    songs = {1: "Unveil.mp3",
             2: "Bookmarks.mp3",
             3: "Nine Times around the Heart.mp3"}
    songs_c = randint(1, 3)
    pygame.mixer.music.load(path.join("assets/music", songs[songs_c]))
    pygame.mixer.music.play(0, 0.0, 3000)
    pygame.mixer.music.set_volume(0.05)

    return songs, songs_c


if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    camera = Camera(WIDTH, HEIGHT)
    player = Player("assets/player/stand_right.png",
                    pygame.transform.scale(load_image("assets/player/stand_right.png"), (640, 64)), 10, 1, 50, 50)

    songs, songs_c = init_music()

    world_map = Map()
    map_image = world_map.make_map()
    map_rect = map_image.get_rect()
    pygame.display.set_caption("Neverland")

    start()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()
        screen.fill(BLACK)

        if not pygame.mixer.music.get_busy():
            songs, songs_c = init_music()

        camera.update(player)

        screen.blit(map_image, (camera.apply_rect(map_rect)))
        for sprite in ALL_SPRITES:
            screen.blit(sprite.image, camera.apply(sprite))

        ALL_SPRITES.update()
        ALL_SPRITES.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)
