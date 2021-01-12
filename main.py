from render import load_level, load_image, Camera, TILE_IMAGES, TILE_WIDTH, TILE_HEIGHT, PLAYER_IMAGES
from settings import *
import sys


def terminate():
    pygame.quit()
    sys.exit()


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player('standing', x, y)
    return new_player, x, y


def add_text_on_screen(*args):
    for texts in args:
        for font, font_size, color, text, x, y, type_text in texts:
            font = pygame.font.Font(font, font_size)
            for line in text:
                if type_text == "centered":
                    string_rendered = font.render(line, True, color)
                    text_rect = string_rendered.get_rect()
                    text_rect.x = (WIDTH - text_rect.width) // 2
                    text_rect.y = y
                    SCREEN.blit(string_rendered, text_rect)


def start_screen():
    SCREEN.fill((0, 0, 0))
    add_text_on_screen([[None, 80, [255, 255, 255], ["Dungeon Adventures"], 0, 50, "centered"]])
    run = True
    while run:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                terminate()
            if ev.type == pygame.KEYDOWN:
                return
        pygame.display.flip()
        CLOCK.tick(FPS)


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        if tile_type == 'wall':
            super().__init__(COLLIDED_TILES_GROUP, ALL_SPRITES)
        else:
            super().__init__(NON_COLLIDED_TILES_GROUP, ALL_SPRITES)
        self.image = TILE_IMAGES[tile_type]
        self.rect = self.image.get_rect().move(
            TILE_WIDTH * pos_x, TILE_HEIGHT * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(PLAYER_GROUP, ALL_SPRITES)
        self.image = PLAYER_IMAGES[tile_type]
        self.rect = self.image.get_rect().move(
            TILE_WIDTH * pos_x + 15, TILE_HEIGHT * pos_y + 5)

    def update(self, *args):
        self.rect = self.rect.move()


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Dungeon Adventures")
        self.level = load_level("level1.txt")
        self.player, self.level_x, self.level_y = self.generate_level(self.level)

    def move_player(self, direction):
        PLAYER_GROUP.remove(self.player)
        ALL_SPRITES.remove(self.player)

        if direction == "left":
            state = True
            for tile in COLLIDED_TILES_GROUP:
                if tile.rect.x == self.player.rect.x - 15 - 50 and tile.rect.y == self.player.rect.y - 5:
                    state = False
                    break
            if state:
                self.player = Player(self.player.pos_x - 1, self.player.pos_y)

        elif direction == "right":
            state = True
            for tile in COLLIDED_TILES_GROUP:
                if tile.rect.x == self.player.rect.x - 15 + 50 and tile.rect.y == self.player.rect.y - 5:
                    state = False
                    break
            if state:
                self.player = Player("right", self.player.pos_x + 1, self.player.pos_y)

        elif direction == "up":
            state = True
            for tile in COLLIDED_TILES_GROUP:
                if tile.rect.x == self.player.rect.x - 15 and tile.rect.y == self.player.rect.y - 5 - 50:
                    state = False
                    break
            if state:
                self.player = Player(self.player.pos_x, self.player.pos_y - 1)

        elif direction == "down":
            state = True
            for tile in COLLIDED_TILES_GROUP:
                if tile.rect.x == self.player.rect.x - 15 and tile.rect.y == self.player.rect.y - 5 + 50:
                    state = False
                    break
            if state:
                self.player = Player(self.player.pos_x, self.player.pos_y + 1)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()
                if event.key == pygame.K_UP:
                    self.move_player("up")
                elif event.key == pygame.K_DOWN:
                    self.move_player("down")
                elif event.key == pygame.K_LEFT:
                    self.move_player("left")
                elif event.key == pygame.K_RIGHT:
                    self.move_player("right")

    def draw(self):
        pygame.display.flip()

    def run(self):
        self.running = True
        while self.running:
            self.events()
            self.draw()
            self.update()

    def generate_level(self, level):
        new_player, x, y = None, None, None
        for y in range(len(level)):
            for x in range(len(level[y])):
                if level[y][x] == '.':
                    Tile('empty', x, y)
                elif level[y][x] == '#':
                    Tile('wall', x, y)
                elif level[y][x] == '@':
                    Tile('empty', x, y)
                    self.new_player = Player("standing", x, y)
        # вернем игрока, а также размер поля в клетках
        return new_player, x, y

    def update(self):
        ALL_SPRITES.update()


if __name__ == "__main__":
    game = Game()
    game.start_screen()
    game.run()
