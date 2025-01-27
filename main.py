import pygame
from _image import load_image
from _load_level import load_level
from _generate_level import generate_level, tiles_group, render
from _start_screen import screen, terminate, start_screen, WIDTH, HEIGHT
from _intermediate_screen import intermediate_screen
from _click import get_cell, movement, count_mouves

pygame.init()

level_map = load_level('map.txt')
generate_level(level_map)

font = pygame.font.Font(None, 90)

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
            count_mouves = movement(pos_old, pos_new, level_map)
            generate_level(level_map)

    fon = pygame.transform.scale(load_image('bubl1.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    render(screen)
    tiles_group.draw(screen)
    screen.blit(font.render(str(count_mouves), True, 'blue'), (10, 5))
    pygame.display.flip()
pygame.quit()
