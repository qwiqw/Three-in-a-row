import pygame
import random


def three_in_a_row(old, new, level):
    print(new)
    print(old, 1)
    print(level[new[1]][new[0]])
    print(level[new[1]][new[0] + 1])
    print(level[new[1]][new[0] + 2])
    if (level[new[1]][new[0]] == level[new[1]][new[0] + 1] and
            level[new[1]][new[0]] == level[new[1]][new[0] + 2]):
        symbol1 = random.choice(['.', '@', '#', '*'])
        symbol2 = random.choice(['.', '@', '#', '*'])
        symbol3 = random.choice(['.', '@', '#', '*'])
        level[new[1]] = level[new[1]][:new[0]] + symbol1 + symbol2 + symbol3 + level[new[1]][new[0] + 3:]
    elif (level[new[1]][new[0]] == level[new[1]][new[0] - 1] and
            level[new[1]][new[0]] == level[new[1]][new[0] - 2]):
        symbol1 = random.choice(['.', '@', '#', '*'])
        symbol2 = random.choice(['.', '@', '#', '*'])
        symbol3 = random.choice(['.', '@', '#', '*'])
        level[new[1]] = level[new[1]][:new[0] - 2] + symbol1 + symbol2 + symbol3 + level[new[1]][new[0] + 1:]


