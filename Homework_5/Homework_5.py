from random import randint

# Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота ""интеллектом""


def Step(sweets):
    step = -1
    while 1 > step or step > 28 or step > sweets:
        step = int(input('Сколько конфет хотите взять? '))
        if not (0 < step < 29):
            print('Введите коректное значение ')
    return  sweets - step


def Sweets_game():
    count = randint(0, 2)
    sweets = 75
    print(f'Всего {sweets} конфет')
    while sweets != 0:
        count += 1
        if count % 2:
            sweets = Step(sweets)
            if sweets == 0:
                return ('you win')
        else:
            if sweets > 28:
                step = (sweets - 1) % 28
                if step == 0:
                    step = randint(0, 29)
                print(step)
                sweets = sweets - step
            else:
                print(f'Соперник взял {sweets} конфет')
                sweets -= sweets
                return ('You lose')
        print(sweets)


print(Sweets_game())

# Сумма многочленов


def Read_pol(file_name):
    file = open(file_name)
    pol = file.read().split(' ')
    file.close()
    return pol


def Sum_poynomials(first_file, second_file):
    polynomial = Read_pol(first_file)
    pol_sum = Pol_in_dict(polynomial)
    polynomial = Read_pol(second_file)
    return Pol_in_dict(polynomial)


def Pol_in_dict(polynomial, polynomial_sum = {}):
    for i in polynomial:
        c = i.split('^')
        if c[0].isnumeric():
            if not polynomial_sum.get(0):
                polynomial_sum[0] = int(c[0])
            else:
                polynomial_sum[0] += int(c[0])
        if len(c) != 1:
            if not polynomial_sum.get(c[1]):
                polynomial_sum[c[1]] = int(c[0].replace('x', ''))
            else:
                polynomial_sum[c[1]] += int(c[0].replace('x', ''))
    return Convert_to_string(polynomial_sum)


def Convert_to_string(prynomial_sum):
    str_polynomial = ""
    key = prynomial_sum.keys()
    for i in key:
        if i != '1' and i != 0:
            str_polynomial += f'{prynomial_sum[i]}x^{i} + '
        elif i == '1':
            str_polynomial += f'{prynomial_sum[i]}x + '
        else:
            str_polynomial += f'{prynomial_sum[i]} '
    str_polynomial += '= 0'
    return str_polynomial

file_name1 = 'first_file.txt'
file_name2 = 'second_file.txt'
f = open('text.txt', 'w')
f.write(Sum_poynomials(file_name1, file_name2))
f.close()


# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
#
# Пример:
#
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
# [1, 5, 2, 3, 4, 1, 7] => [1, 5]


def Get_increase_row(consistency):
    increase = [consistency[0]]
    for i in consistency:
        if increase[-1] < i:
            increase.append(i)
    return increase


consistency = [1, 5, 2, 3, 4, 6, 1, 7]
print(consistency)
print(Get_increase_row(consistency))

