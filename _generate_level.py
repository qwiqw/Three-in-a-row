import pygame
from _image import load_image

all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
tile_width = tile_height = 50
left = 90
cell_size = 51
top = 134

tile_images = {
    'hanos': pygame.transform.scale(load_image('fishes/hanos.jpg'), (48, 48)),
    'goldcrucian': pygame.transform.scale(load_image('fishes/goldcrucian.jpg'), (48, 48)),
    'redsnap': pygame.transform.scale(load_image('fishes/redsnap.jpg'), (48, 48)),
    'catfish': pygame.transform.scale(load_image('fishes/catfish.jpg'), (48, 48)),
}


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + left + 1 + pos_x, tile_height * pos_y + top + 1 + pos_y)


def render(screen):
    for y in range(9):
        for x in range(9):
            pygame.draw.rect(screen, 'blue', (left + cell_size * x, top
                                              + cell_size * y, cell_size, cell_size), 1)


def generate_level(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('hanos', x, y)
            elif level[y][x] == '#':
                Tile('goldcrucian', x, y)
            elif level[y][x] == '@':
                Tile('redsnap', x, y)
            elif level[y][x] == '*':
                Tile('catfish', x, y)
    return
