from render import load_level, load_image, generate_level, Camera
from settings import *


def terminate():
    pygame.quit()
    sys.exit()


def add_text(*args):
    for texts in args:
        for font_size, color, text, x, y, type_text in texts:
            font = pygame.font.Font(None, font_size)
            for line in text:
                if type_text == "centered":
                    string_rendered = font.render(line, True, color)
                    text_rect = string_rendered.get_rect()
                    text_rect.x = (WIDTH - text_rect.width) // 2
                    text_rect.y = y
                    SCREEN.blit(string_rendered, text_rect)


def start_screen():
    pygame.init()
    SCREEN.fill((0, 0, 0))
    add_text([[80, [255, 255, 255], ["Dungeon Adventures"], 0, 50, "centered"]])

    run = True
    while run:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                terminate()
            if ev.type == pygame.KEYDOWN:
                return
        pygame.display.flip()
        CLOCK.tick(FPS)


if __name__ == "__main__":
    start_screen()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        pygame.display.flip()
        CLOCK.tick(FPS)

    pygame.quit()
