from settings import *
import pytmx
import pygame


class Map:
    def __init__(self):
        self.map = pytmx.load_pygame("assets/maps/map.tmx")
        self.width = self.map.width * self.map.tilewidth
        self.height = self.map.height * self.map.tileheight
        print(self.width, self.height)

    def render(self, screen):
        map_image = self.map.get_tile_image_by_gid
        for l in self.map.visible_layers:
            if isinstance(l, pytmx.TiledTileLayer):
                for x, y, gid in l:
                    tile = map_image(gid)
                    if tile:
                        screen.blit(tile, (x * TILESIZE, y * TILESIZE))

    def make_map(self):
        surf = pygame.Surface((self.width, self.height))
        self.render(surf)
        return surf
