import pygame
import random


def three_in_a_row(old, new, level):
    if (level[new[1]][new[0]] == level[new[1]][new[0] + 1] and
            level[new[1]][new[0]] == level[new[1]][new[0] + 2] and
            level[new[1]][new[0]] == level[new[1]][new[0] - 1] and
            level[new[1]][new[0]] == level[new[1]][new[0] - 2]):
        print('5 in row x')
    elif (level[new[1]][new[0]] == level[new[1] + 1][new[0]] and
            level[new[1]][new[0]] == level[new[1] + 2][new[0]] and
            level[new[1]][new[0]] == level[new[1] - 1][new[0]] and
            level[new[1]][new[0]] == level[new[1] - 2][new[0]]):
        print('5 in row y')
    elif (level[new[1]][new[0]] == level[new[1]][new[0] + 1] and
            level[new[1]][new[0]] == level[new[1]][new[0] + 2] and
            level[new[1]][new[0]] == level[new[1]][new[0] - 1]):
        print('4 in row x')
    elif (level[new[1]][new[0]] == level[new[1]][new[0] - 1] and
            level[new[1]][new[0]] == level[new[1]][new[0] - 2] and
            level[new[1]][new[0]] == level[new[1]][new[0] + 1]):
        print('4 in row x')
    elif (level[new[1]][new[0]] == level[new[1]][new[0] + 1] and
            level[new[1]][new[0]] == level[new[1]][new[0] + 2]):
        symbol1 = level[new[1] - 1][new[0]]
        symbol2 = level[new[1] - 1][new[0] + 1]
        symbol3 = level[new[1] - 1][new[0] + 2]
        level[new[1]] = level[new[1]][:new[0]] + symbol1 + symbol2 + symbol3 + level[new[1]][new[0] + 3:]
    elif (level[new[1]][new[0]] == level[new[1]][new[0] - 1] and
            level[new[1]][new[0]] == level[new[1]][new[0] - 2]):
        symbol1 = level[new[1] - 1][new[0] - 2]
        symbol2 = level[new[1] - 1][new[0] - 1]
        symbol3 = level[new[1] - 1][new[0]]
        level[new[1]] = level[new[1]][:new[0] - 2] + symbol1 + symbol2 + symbol3 + level[new[1]][new[0] + 1:]
    elif (level[new[1]][new[0]] == level[new[1]][new[0] - 1] and
            level[new[1]][new[0]] == level[new[1]][new[0] + 1]):
        symbol1 = level[new[1] - 1][new[0] - 1]
        symbol2 = level[new[1] - 1][new[0]]
        symbol3 = level[new[1] - 1][new[0] + 1]
        level[new[1]] = level[new[1]][:new[0] - 1] + symbol1 + symbol2 + symbol3 + level[new[1]][new[0] + 2:]
    elif (level[new[1]][new[0]] == level[new[1] - 1][new[0]] and
            level[new[1]][new[0]] == level[new[1] + 1][new[0]]):
        print('centr y')
    elif (level[new[1]][new[0]] == level[new[1] - 1][new[0]] and
            level[new[1]][new[0]] == level[new[1] - 2][new[0]]):
        print('up y')
    elif (level[new[1]][new[0]] == level[new[1] + 1][new[0]] and
            level[new[1]][new[0]] == level[new[1] + 2][new[0]]):
        print('down y')


