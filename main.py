import pygame
from _image import load_image
from _load_level import load_level
from _generate_level import generate_level, tiles_group, render
from _start_screen import screen, terminate, start_screen, WIDTH, HEIGHT
from _intermediate_screen import intermediate_screen
from _click import get_cell, movement, count_mouves
from _catalog_levels import catalog_screen

pygame.init()

font = pygame.font.Font(None, 90)

pos_old = (0, 0)
pos_new = (0, 0)

start_screen()
intermediate_screen()
level_map = load_level(catalog_screen())
generate_level(level_map)
intermediate_screen()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            pos_old = get_cell(pos)

        if event.type == pygame.MOUSEBUTTONUP:
            pos = event.pos
            pos_new = get_cell(pos)
            count_mouves = movement(pos_old, pos_new, level_map)
            generate_level(level_map)

    fon = pygame.transform.scale(load_image('bubbles/bubl1.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    render(screen)
    tiles_group.draw(screen)
    screen.blit(font.render(str(count_mouves), True, (255, 193, 193)), (40, 40))
    pygame.display.flip()
pygame.quit()
