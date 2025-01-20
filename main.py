import pygame
import sys
import os

pygame.init()

FPS = 50
WIDTH, HEIGHT = size = 550, 550
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


def terminate():
    pygame.quit()
    sys.exit()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    return list(level_map)


tile_images = {
    'herring': pygame.transform.scale(load_image('1.jpg'), (50, 50)),
    'carp': pygame.transform.scale(load_image('2.jpg'), (50, 50)),
    'redfish': pygame.transform.scale(load_image('3.jpg'), (50, 50)),
    'som': pygame.transform.scale(load_image('4.jpg'), (50, 50)),
}

tile_width = tile_height = 50

all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()


def generate_level(level):
    x, y = None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('herring', x, y)
            elif level[y][x] == '#':
                Tile('carp', x, y)
            elif level[y][x] == '@':
                Tile('redfish', x, y)
            elif level[y][x] == '*':
                Tile('som', x, y)
    return


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


level_map = load_level('map.txt')
generate_level(level_map)


def start_screen():
    intro_text = [""]
    fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)


def mousepos(pos):
    x, y = pos
    print((x // 50) + 1, (y // 50) + 1)
    return (x // 50) + 1, (y // 50) + 1


start_screen()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            mousepos(pos)

    screen.fill('white')
    tiles_group.draw(screen)
    pygame.display.flip()
pygame.quit()
