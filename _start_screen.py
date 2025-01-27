import pygame
import sys
from _image import load_image

FPS = 50
clock = pygame.time.Clock()
WIDTH, HEIGHT = size = 650, 650
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Russian fishing')


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    fon = pygame.transform.scale(load_image('bubl1.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))

    font_title = pygame.font.Font(None, 70)
    text_title = font_title.render('Russian fishing', True, 'white')

    font_btn = pygame.font.Font(None, 50)
    text_btn = font_btn.render('Start', True, 'white')

    button_rect = pygame.Rect(370, 280, 140, 70)
    pygame.draw.rect(screen, 'white', button_rect, 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return
        screen.blit(text_title, (180, 100))
        screen.blit(text_btn, (400, 300))
        pygame.display.flip()
        clock.tick(FPS)