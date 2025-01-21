import pygame
from _load_level import load_level
from _generate_level import generate_level, tiles_group
from _start_screen import screen, terminate, start_screen
from _intermediate_screen import intermediate_screen

pygame.init()

level_map = load_level('map.txt')
generate_level(level_map)


def mousepos(pos):
    x, y = pos
    print((x // 50) + 1, (y // 50) + 1)
    return (x // 50) + 1, (y // 50) + 1


start_screen()
intermediate_screen()
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
