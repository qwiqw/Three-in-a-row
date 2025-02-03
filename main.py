import pygame
from _image import load_image
from _load_level import load_level
from _generate_level import generate_level, tiles_group, render, top, left, cell_size
from _start_screen import screen, terminate, start_screen, WIDTH, HEIGHT
from _intermediate_screen import intermediate_screen
from _click import movement, count_mouves
from _catalog_levels import catalog_screen
from _three_in_a_row import three_in_a_row
from _search_coords import get_cell
from _final_screen import winner
from _music import music_and_sound

pygame.init()

font = pygame.font.Font(None, 90)

pos_old = (0, 0)
pos_new = (0, 0)

music_and_sound()

start_screen()
intermediate_screen()
level_map = load_level(catalog_screen())
generate_level(level_map)
intermediate_screen()
running = True
box = pygame.Rect(left, top, cell_size * 9, cell_size * 9)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()

        if event.type == pygame.MOUSEBUTTONDOWN and box.collidepoint(event.pos):
            pos = event.pos
            pos_old = get_cell(pos)

        if event.type == pygame.MOUSEBUTTONUP and box.collidepoint(event.pos):
            pos = event.pos
            pos_new = get_cell(pos)
            count_mouves = movement(pos_old, pos_new, level_map)
            three_in_a_row(pos_old, pos_new, level_map)
            generate_level(level_map)

    fon = pygame.transform.scale(load_image('bubbles/bubl1.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    render(screen)
    tiles_group.draw(screen)
    screen.blit(font.render(str(count_mouves), True, (255, 193, 193)), (40, 40))
    screen.blit(font.render(str(count_mouves * 52), True, (255, 193, 193)), (500, 40))
    winner(count_mouves)
    pygame.display.flip()
pygame.quit()
