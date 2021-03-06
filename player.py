from settings import *
import pygame
import os
import pygame
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join(name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Player(pygame.sprite.Sprite):
    def __init__(self, image, sheet, columns, rows, x, y):
        super().__init__(PLAYER_SPRITE)
        self.frames = []
        self.pos = self.x, self.y = x, y
        self.direction = "right"
        self.image_name = image

        self.sheet = sheet
        self.columns = columns
        self.rows = rows
        self.moved = False
        self.anim_changed = False
        self.collide_up, self.collide_right, self.collide_left, self.collide_down = False, False, False, False

        self.cut_sheet(self.sheet, columns, rows)

        self.c = 0
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(self.x, self.y, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        self.frames = []
        self.cur_frame = 0
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def change_animations(self):
        if self.image_name == "assets/player/stand_right.png" or self.image_name == "assets/player/stand_left.png":
            if self.direction == "right":
                self.image_name = "assets/player/run_right.png"
                self.sheet = pygame.transform.scale(load_image("assets/player/run_right.png"), (640, 64))
            else:
                self.image_name = "assets/player/run_left.png"
                self.sheet = pygame.transform.scale(load_image("assets/player/run_left.png"), (640, 64))
            self.cut_sheet(self.sheet, self.columns, self.rows)
        else:
            if self.direction == "right":
                self.image_name = "assets/player/stand_right.png"
                self.sheet = pygame.transform.scale(load_image("assets/player/stand_right.png"), (640, 64))
            else:
                self.image_name = "assets/player/stand_left.png"
                self.sheet = pygame.transform.scale(load_image("assets/player/stand_left.png"), (640, 64))
            self.cut_sheet(self.sheet, self.columns, self.rows)

    def update(self):
        self.c += 1
        if self.c == 5:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]
            self.c = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            if not self.collide_left:
                self.x -= PLAYER_SPEED
                self.moved = True
            self.direction = "left"

            if self.image_name == "assets/player/stand_left.png" or self.image_name == "assets/player/stand_right.png":
                if not self.anim_changed:
                    self.change_animations()
                    self.anim_changed = True

        if keys[pygame.K_d]:
            if not self.collide_right:
                self.x += PLAYER_SPEED
                self.moved = True
            self.direction = "right"

            if self.image_name == "assets/player/stand_left.png" or self.image_name == "assets/player/stand_right.png":
                if not self.anim_changed:
                    self.change_animations()
                    self.anim_changed = True

        if keys[pygame.K_w]:
            if not self.collide_up:
                self.y -= PLAYER_SPEED
                self.moved = True

            if self.image_name == "assets/player/stand_left.png" or self.image_name == "assets/player/stand_right.png":
                self.change_animations()

        if keys[pygame.K_s]:
            if not self.collide_down:
                self.y += PLAYER_SPEED
                self.moved = True

            if self.image_name == "assets/player/stand_left.png" or self.image_name == "assets/player/stand_right.png":
                self.change_animations()

        if not self.moved:
            if self.image_name == "assets/player/run_left.png" or self.image_name == "assets/player/run_right.png":
                if not self.anim_changed:
                    self.change_animations()

        self.moved = False
        self.anim_changed = False
        self.collide_up, self.collide_right, self.collide_left, self.collide_down = False, False, False, False

        self.rect.x = self.x
        self.rect.y = self.y


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, name):
        super().__init__(ALL_SPRITES)
        self.image = pygame.Surface((0, 0))
        self.rect = pygame.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.name = name

        self.rect.x = x
        self.rect.y = y


class Interact(pygame.sprite.Sprite):
    def __init__(self, name, image, sheet, columns, rows, x, y):
        super().__init__(OTHER_SPRITES)
        self.frames = []
        self.pos = self.x, self.y = x, y

        self.name = name
        self.image_name = image
        self.sheet = sheet
        self.columns = columns
        self.rows = rows

        self.displayed = True
        self.wait = False

        self.cut_sheet(self.sheet, self.columns, self.rows)

        self.c = 0
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(self.x, self.y, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        self.frames = []
        self.cur_frame = 0
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self, *args):
        player_x, player_y = args[0]
        if self.displayed:
            self.c += 1
            if self.c == 3 and not self.wait:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames)
                self.image = self.frames[self.cur_frame]
                self.c = 0
                if self.cur_frame + 1 == len(self.frames):
                    self.wait = True
            elif self.c >= 250:
                self.displayed = False
        self.rect.x = player_x + 10
        self.rect.y = player_y - 95

