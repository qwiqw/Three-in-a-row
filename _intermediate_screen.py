import pygame
from _image import load_image
from _start_screen import screen, terminate, WIDTH, HEIGHT, clock, FPS


def intermediate_screen():
    gap = pygame.transform.scale(load_image('slide.jpg'), (WIDTH, HEIGHT))
    screen.blit(gap, (0, 0))
    x, y = 0, 550
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill('black')
        y -= 8
        screen.blit(gap, (x, y))
        if y < 0:
            return
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
