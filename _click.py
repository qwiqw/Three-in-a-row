import pygame

all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
tile_width = tile_height = 50
left = 40
cell_size = 51
top = 50
count_mouves = 0


def get_cell(mouse_pos):
    x, y = mouse_pos
    return ((x - left) // cell_size, (y - top) // cell_size)


def movement(old, new, level):
    global count_mouves
    if (old[0] < 0 or old[0] > 8 or old[1] < 0 or old[1] > 8
            or new[0] < 0 or new[0] > 8 or new[1] < 0 or new[1] > 8):
        return count_mouves

    if level[old[1]][old[0]] == level[new[1]][new[0]]:
        return count_mouves

    if old[0] == new[0] + 1 and old[1] == new[1]:
        level[old[1]] = (level[old[1]][:(new[0])] + level[old[1]][old[0]]
                         + level[new[1]][new[0]] + level[old[1]][(new[0] + 2):])
        count_mouves += 1

    if old[0] == new[0] - 1 and old[1] == new[1]:
        level[old[1]] = (level[old[1]][:(old[0])] + level[new[1]][new[0]] + level[old[1]][old[0]]
                         + level[old[1]][(old[0] + 2):])
        count_mouves += 1

    if old[1] == new[1] - 1 and old[0] == new[0] or old[1] == new[1] + 1 and old[0] == new[0]:
        oldfish = level[old[1]][old[0]]
        level[old[1]] = level[old[1]][:(old[0])] + level[new[1]][new[0]] + level[old[1]][(old[0] + 1):]
        level[new[1]] = level[new[1]][:(new[0])] + oldfish + level[new[1]][(new[0] + 1):]
        count_mouves += 1
    return count_mouves
