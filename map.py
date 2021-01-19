from settings import *

text_map = [
    '############',
    '#..........#',
    '#..........#',
    '#..........#',
    '#..........#',
    '#..........#',
    '#..........#',
    '############'
]

world_map = set()
for i, row in enumerate(text_map):
    for j, letter in enumerate(row):
        if letter == "#":
            world_map.add((j * TILESIZE, i * TILESIZE))