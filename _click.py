import pygame

all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
tile_width = tile_height = 50
left = 40
cell_size = 51
top = 50


def get_cell(mouse_pos):
    x, y = mouse_pos
    if (x < left or x > 9 * cell_size + left or
            y < top or y > 9 * cell_size + top):
        return None
    else:
        return ((x - left) // cell_size + 1, (y - top) // cell_size + 1)
