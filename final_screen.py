import pygame
import sys
from _image import load_image

FPS = 50
clock = pygame.time.Clock()
WIDTH, HEIGHT = size = 650, 650
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Russian fishing')


def winner(count_mouves):
    if count_mouves * 52 >= 100:
        final_screen()


def terminate():
    pygame.quit()
    sys.exit()


def final_screen():
    fon = pygame.transform.scale(load_image('bubbles/bubl1.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))

    font = pygame.font.Font(None, 100)
    text = font.render('you are winner', True, (244, 193, 193))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

        screen.blit(text, (120, 225))
        pygame.display.flip()
        clock.tick(FPS)
