import pygame
from _load_level import load_level
from _generate_level import generate_level, tiles_group, render
from _start_screen import screen, terminate, start_screen
from _intermediate_screen import intermediate_screen
from _click import get_cell, movement


pygame.init()

level_map = load_level('map.txt')
print(level_map)
generate_level(level_map)

pos_old = (0, 0)
pos_new = (0, 0)

start_screen()
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
            movement(pos_old, pos_new, level_map)
            generate_level(level_map)

    screen.fill('white')
    render(screen)
    tiles_group.draw(screen)
    pygame.display.flip()
pygame.quit()
