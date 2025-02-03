import pygame

pygame.init()


def music_and_sound():
    pygame.mixer.music.load('data/music/london_music_orc.wav')
    pygame.mixer.music.play()