from random import randint

cell = [" " for i in range(9)]
win_combination = [(0, 1, 2), (0, 4, 8), (0, 3, 6), (1, 4, 7), (2, 4, 6), (2, 5, 8), (3, 4, 5), (6, 7, 8)]


def Game():
    turn = randint(0, 2)
    while True:
        if turn % 2 == 0:
            Player_Step(cell)
            if Check_end(cell, mark='X'):
                return ('X - win')
        else:
            Bot_step(cell)
            if Check_end(cell, mark='0'):
                return ('0 - win')
        turn += 1


def Bot_step(cell):
    step = randint(0, 8)
    while cell[step] != " ":
        step = randint(0, 8)
    cell[step] = '0'
    Print(cell)
    return cell


def Check_end(cell, mark):
    for i in win_combination:
        count = 0
        for k in i:
            if cell[k] == mark:
                count += 1
                if count == 3:
                    return True
    return False


def Player_Step(cell):
    step = int(input(('Введите ячейку ')))
    while cell[step] != ' ':
        step = int(input('Введите ячейку '))
    cell[step] = 'X'
    Print(cell)
    return cell


def Print(cell):
    print(f'{cell[0]:^5}|{cell[1]:^5}|{cell[2]:^5}')
    print('-----------------')
    print(f'{cell[3]:^5}|{cell[4]:^5}|{cell[5]:^5}')
    print('-----------------')
    print(f'{cell[6]:^5}|{cell[7]:^5}|{cell[8]:^5}')


print(Game())