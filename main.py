import pygame
import sys
from random import randint
from os import path
from settings import *
from player import load_image, Player, Obstacle, Interact
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


def start(player_pos, player_name):
    pygame.init()

    ALL_SPRITES = pygame.sprite.Group()
    PLAYER_SPRITE = pygame.sprite.Group()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    world_map = Map()
    obstacles = []
    camera = Camera(world_map.width, world_map.height)
    collide_up, collide_right, collide_left, collide_down = False, False, False, False
    interact_hole, interact_house, interact_lava, interact_dirt, interact_lake, interact_city = False, False, False, \
                                                                                                False, False, False

    for obstacle in world_map.map.objects:
        print(obstacle.x, obstacle.y, obstacle.width, obstacle.height, obstacle.name)
        if cur_map == "map.tmx":
            if obstacle.name == player_name:
                player = Player("assets/player/stand_right.png",
                                pygame.transform.scale(load_image("assets/player/stand_right.png"), (640, 64)),
                                10, 1, player_pos[0], player_pos[1])
                PLAYER_SPRITE.add(player)
            else:
                obs = Obstacle(int(obstacle.x), int(obstacle.y), int(obstacle.width), int(obstacle.height),
                               obstacle.name)
                ALL_SPRITES.add(obs)
                obstacles.append(obs)

        else:
            if obstacle.name == player_name:
                player = Player("assets/player/stand_right.png",
                                pygame.transform.scale(load_image("assets/player/stand_right.png"), (640, 64)),
                                10, 1, player_pos[0], player_pos[1])
            else:
                obstacles.append(Obstacle(int(obstacle.x), int(obstacle.y), int(obstacle.width), int(obstacle.height),
                                          obstacle.name))

    songs, songs_c = init_music()

    map_image = world_map.make_map()
    map_rect = map_image.get_rect()
    pygame.display.set_caption("Neverland")

    return ALL_SPRITES, PLAYER_SPRITE, screen, world_map, clock, obstacles, camera, collide_up, collide_down, \
           collide_left, collide_right, interact_hole, interact_house, interact_lava, interact_dirt, interact_lake, \
           interact_city, player, songs, songs_c, map_image, map_rect


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
    clock = pygame.time.Clock()

    if not start_screen(screen, clock):
        terminate()

    cur_map = "map.tmx"
    change_map = False
    player_pos = (512, 512)
    player_name = "player"
    names = []
    dialog_sprites = []
    to_add = True

    ALL_SPRITES, PLAYER_SPRITE, screen, world_map, clock, obstacles, camera, collide_up, collide_down, collide_left, \
    collide_right, interact_hole, interact_house, interact_lava, interact_dirt, interact_lake, \
    interact_city, player, songs, songs_c, map_image, map_rect = start(player_pos, player_name)

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

        player_x, player_y = camera.update(player)

        screen.blit(map_image, (camera.apply_rect(map_rect)))
        for sprite in ALL_SPRITES:
            screen.blit(sprite.image, camera.apply(sprite))

        for sprite in obstacles:
            if pygame.sprite.collide_rect(player, sprite):
                if sprite.name == "obstacle" or sprite.name == "hole":
                    print(f"Пересечение игрока {player.rect.x, player.rect.y, player.rect.width, player.rect.height} с "
                          f"объектом {sprite.rect.x, sprite.rect.y, sprite.rect.width, sprite.rect.height}")
                    if player.rect.x < sprite.rect.x:
                        player.collide_right = True
                        print(f"right: {player.collide_right}")
                    if player.rect.x > sprite.rect.x:
                        player.collide_left = True
                        print(f"left: {player.collide_left}")
                    if player.rect.y > sprite.rect.y:
                        player.collide_up = True
                        print(f"down: {player.collide_up}")
                    if player.rect.y < sprite.rect.y:
                        player.collide_down = True
                        print(f"up: {player.collide_down}")
                elif sprite.name:
                    if sprite.name[:8] == "interact":
                        if not (sprite.name.split("_")[-1] in names):
                            names.append(sprite.name.split("_")[-1])
                            print("Новая реплика: " + sprite.name)

        print(f"Игрок: {player.rect.x}, {player.rect.y}")

        ALL_SPRITES.update()
        PLAYER_SPRITE.update()

        cur_x, cur_y = player.rect.x, player.rect.y
        if player_y != 0:
            player.rect.y = player_y
        if player_x != 0:
            player.rect.x = player_x
        if camera.player_at_bottom_side:
            player.rect.y = 1080 - (world_map.height - player.rect.y)
        if camera.player_at_right_side:
            player.rect.x = 1920 - (world_map.width - player.rect.x)
        print(f"{player.rect.x}, {player.rect.y} - игрок на камере")

        OTHER_SPRITES.update((player.rect.x, player.rect.y))
        PLAYER_SPRITE.draw(screen)

        for name in names:
            print(dialog_sprites)
            print(names)
            for sprite in dialog_sprites:
                if sprite.name == name:
                    if name in names:
                        names.remove(name)

        for name in names:
            dialog_sprites.append(Interact(name, "assets/dialog icons/interact_" + name + ".png",
                                           pygame.transform.scale(
                                               load_image("assets/dialog icons/interact_" + name
                                                          + ".png"), (1401, 105)), 6, 1, player.rect.x + 10,
                                           player.rect.y - 95))
            print(name + " был добавлен")
        name = []

        OTHER_SPRITES.empty()

        for sprite in dialog_sprites:
            if sprite.displayed:
                OTHER_SPRITES.add(sprite)

        OTHER_SPRITES.draw(screen)

        player.rect.y = cur_y
        player.rect.x = cur_x

        print("-------------------")

        pygame.display.flip()
        clock.tick(FPS)
