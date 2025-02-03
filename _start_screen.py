import pygame
import sys
from _image import load_image
from _settings import screen_settings

pygame.init()

FPS = 50
clock = pygame.time.Clock()
WIDTH, HEIGHT = size = 650, 650
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Russian fishing')


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    fon = pygame.transform.scale(load_image('bubbles/bubl1.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))

    font_title = pygame.font.Font(None, 70)
    text_title = font_title.render('Russian fishing', True, (244, 193, 193))

    font_btn = pygame.font.Font(None, 50)
    text_btn = font_btn.render('Start', True, (244, 193, 193))

    button_rect = pygame.Rect(250, 280, 140, 70)

    button_settings_rect = pygame.Rect(550, 30, 70, 70)
    button_settings_image = pygame.transform.scale(load_image('other/settings.jpg'), (70, 70))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return
                elif button_settings_rect.collidepoint(event.pos):
                    screen_settings()
        pygame.draw.rect(screen, (244, 193, 193), button_rect, 3)
        screen.blit(button_settings_image, (550, 30))
        screen.blit(text_title, (130, 150))
        screen.blit(text_btn, (280, 300))
        pygame.draw.rect(screen, (244, 193, 193), button_settings_rect, 3)
        pygame.display.flip()
        clock.tick(FPS)
