from settings import *
import pytmx

level1_text_map = pytmx.load_pygame("assets/maps/level1.tmx")

level1_map = set()
for i, row in enumerate(level1_text_map):
    for j, letter in enumerate(row):
        if letter == "#":
            level1_map.add((j * TILESIZE, i * TILESIZE))
