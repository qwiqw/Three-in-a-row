import pygame
from _start_screen import screen, terminate, WIDTH, HEIGHT, FPS, clock
from _image import load_image


def catalog_screen():
    fon = pygame.transform.scale(load_image('bubbles/bubl1.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))

    font_title = pygame.font.Font(None, 80)
    text_title = font_title.render('Russian fishing', True, (244, 193, 193))

    font_btn1 = pygame.font.Font(None, 70)
    text_btn1 = font_btn1.render('1', True, (244, 193, 193))

    button_rect1 = pygame.Rect(180, 150, 70, 70)
    pygame.draw.rect(screen, (244, 193, 193), button_rect1, 3)

    font_btn2 = pygame.font.Font(None, 70)
    text_btn2 = font_btn2.render('2', True, (244, 193, 193))

    button_rect2 = pygame.Rect(280, 150, 70, 70)
    pygame.draw.rect(screen, (244, 193, 193), button_rect2, 3)

    font_btn3 = pygame.font.Font(None, 70)
    text_btn3 = font_btn3.render('3', True, (244, 193, 193))

    button_rect3 = pygame.Rect(380, 150, 70, 70)
    pygame.draw.rect(screen, (244, 193, 193), button_rect3, 3)

    font_btn4 = pygame.font.Font(None, 70)
    text_btn4 = font_btn4.render('4', True, (244, 193, 193))

    button_rect4 = pygame.Rect(230, 250, 70, 70)
    pygame.draw.rect(screen, (244, 193, 193), button_rect4, 3)

    font_btn5 = pygame.font.Font(None, 70)
    text_btn5 = font_btn5.render('5', True, (244, 193, 193))

    button_rect5 = pygame.Rect(330, 250, 70, 70)
    pygame.draw.rect(screen, (244, 193, 193), button_rect5, 3)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect1.collidepoint(event.pos):
                    return 'map1.txt'
                if button_rect2.collidepoint(event.pos):
                    return 'map2.txt'
                if button_rect3.collidepoint(event.pos):
                    return 'map3.txt'
                if button_rect4.collidepoint(event.pos):
                    return 'map4.txt'
                if button_rect5.collidepoint(event.pos):
                    return 'map5.txt'
        screen.blit(text_title, (125, 50))
        screen.blit(text_btn1, (201, 162))
        screen.blit(text_btn2, (301, 162))
        screen.blit(text_btn3, (401, 162))
        screen.blit(text_btn4, (251, 262))
        screen.blit(text_btn5, (351, 262))
        pygame.display.flip()
        clock.tick(FPS)
