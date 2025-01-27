import pygame
from _image import load_image
from _start_screen import screen, WIDTH, HEIGHT, clock


def intermediate_screen():
    images = []
    count_passes = 0
    for i in range(1, 27 + 1):
        images.append(pygame.transform.scale(load_image(f'bubl{i}.png'), (WIDTH, HEIGHT)))

    animation_length = len(images)
    animation_speed = 20
    index_image = 0
    animation_timer = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        time_change = clock.tick(60) / 1000
        animation_timer += time_change

        if animation_timer >= 1.0 / animation_speed:
            index_image = (index_image + 1) % animation_length
            animation_timer -= 1.0 / animation_speed

        current_frame = images[index_image]
        screen.blit(current_frame, (0, 0))

        if index_image == 26:
            count_passes += 1
            if count_passes == 5:
                return

        pygame.display.flip()
    pygame.quit()