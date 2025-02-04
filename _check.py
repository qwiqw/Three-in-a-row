import random

def check(level):
    for y in range(9):
        for x in range(1, 7):
            if level[y][x] == level[y][x - 1] == level[y][x + 1]:
                choice_list = ['.', '@', '#', '*']
                symbol1 = random.choice(choice_list)
                choice_list.remove(symbol1)
                symbol2 = random.choice(choice_list)
                choice_list.remove(symbol2)
                symbol3 = random.choice(choice_list)
                level[y] = level[y][:x - 1] + symbol1 + symbol2 + symbol3 + level[y][x + 2:]
    for y in range(1, 7):
        for x in range(9):
            if level[y][x] == level[y + 1][x] == level[y - 1][x]:
                choice_list = ['.', '@', '#', '*']
                symbol1 = random.choice(choice_list)
                choice_list.remove(symbol1)
                symbol2 = random.choice(choice_list)
                choice_list.remove(symbol2)
                symbol3 = random.choice(choice_list)
                level[y - 1] = level[y - 1][:x] + symbol1 + level[y - 1][x + 1:]
                level[y] = level[y][:x] + symbol2 + level[y][x + 1:]
                level[y + 1] = level[y + 1][:x] + symbol3 + level[y + 1][x + 1:]

