import pygame

pygame.init()

size = wight, height = 1000, 600

pygame.display.set_caption('Russian fishing')
screen = pygame.display.set_mode(size)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill('black')

    pygame.display.flip()
pygame.quit()
