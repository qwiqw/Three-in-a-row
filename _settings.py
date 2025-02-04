import pygame
import sys
from _image import load_image

FPS = 50
clock = pygame.time.Clock()
WIDTH, HEIGHT = size = 650, 650
screen = pygame.display.set_mode(size)


def terminate():
    pygame.quit()
    sys.exit()


def screen_settings():
    fon = pygame.transform.scale(load_image('bubbles/bubl1.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font_btn1 = pygame.font.Font(None, 50)
    text_btn1 = font_btn1.render('Music OFF', True, (244, 193, 193))
    button_rect1 = pygame.Rect(220, 280, 210, 70)
    pygame.draw.rect(screen, (244, 193, 193), button_rect1, 3)

    font_btn2 = pygame.font.Font(None, 50)
    text_btn2 = font_btn2.render('Music ON', True, (244, 193, 193))
    button_rect2 = pygame.Rect(220, 180, 210, 70)
    pygame.draw.rect(screen, (244, 193, 193), button_rect2, 3)

    font_btn_back = pygame.font.Font(None, 50)
    text_btn_back = font_btn_back.render('BACK', True, (244, 193, 193))
    button_rect_back = pygame.Rect(500, 30, 120, 70)
    pygame.draw.rect(screen, (244, 193, 193), button_rect_back, 3)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect1.collidepoint(event.pos):
                    pygame.mixer.music.stop()
                if button_rect2.collidepoint(event.pos):
                    pygame.mixer.music.play()
                if button_rect_back.collidepoint(event.pos):
                    screen.blit(fon, (0, 0))
                    return
        screen.blit(text_btn1, (240, 300))
        screen.blit(text_btn2, (240, 200))
        screen.blit(text_btn_back, (510, 50))
        pygame.display.flip()
        clock.tick(FPS)
