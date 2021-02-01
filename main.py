import pygame
import sys
from random import randint
from os import path
from settings import *
from player import load_image, Player, Obstacle
from render import Camera
from map import Map


def terminate():
    pygame.quit()
    sys.exit()


def start_screen(screen, clock):
    background = load_image("assets/map icons/background.png")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    font_name = path.join("assets/font", "18177.otf")
    font1 = pygame.font.Font(font_name, 80)
    text = ("Neverland", "",
            "Press any key to continue")
    text_coord = 30
    screen.blit(background, (0, 0))
    for line in text:
        string_rendered = font1.render(line, 1, BLUE)
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
    songs = {1: "Bookmarks.mp3",
             2: "Nine Times around the Heart.mp3"}
    songs_c = randint(1, 2)
    pygame.mixer.music.load(path.join("assets/music", songs[songs_c]))
    pygame.mixer.music.set_endevent(MUSIC_EVENT)
    pygame.mixer.music.play(0, 0.0, 3000)
    pygame.mixer.music.set_volume(0.05)

    return songs, songs_c


if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    world_map = Map()
    clock = pygame.time.Clock()
    obstacles = []
    camera = Camera(world_map.width, world_map.height)

    for obstacle in world_map.map.objects:
        print(obstacle.x, obstacle.y, obstacle.width, obstacle.height)
        if obstacle.name != "player":
            obstacles.append(Obstacle(int(obstacle.x), int(obstacle.y), int(obstacle.width), int(obstacle.height)))
        else:
            player = Player("assets/player/stand_right.png",
                            pygame.transform.scale(load_image("assets/player/stand_right.png"), (640, 64)),
                            10, 1, 1600, 900)

    songs, songs_c = init_music()

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
            if event.type == MUSIC_EVENT:
                songs, songs_c = init_music()

        screen.fill(BLACK)

        camera.update(player)

        screen.blit(map_image, (camera.apply_rect(map_rect)))
        for sprite in ALL_SPRITES:
            screen.blit(sprite.image, camera.apply(sprite))

        for sprite in obstacles:
            if pygame.sprite.collide_rect(player, sprite):
                print(f"Пересечение игрока ({player.rect.x, player.rect.y, player.rect.width, player.rect.height}) с "
                      f"объектом ({sprite.rect.x, sprite.rect.y, sprite.rect.width, sprite.rect.height})")
        print(f"Игрок: {player.rect.x}, {player.rect.y}")

        ALL_SPRITES.update()
        PLAYER_SPRITE.update()
        PLAYER_SPRITE.draw(screen)

        if pygame.sprite.spritecollide(player, ALL_SPRITES, False):
            player.can_move = False

        pygame.display.flip()
        clock.tick(FPS)
