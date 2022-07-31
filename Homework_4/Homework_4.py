import math
from random import randint


# d = int(input('Vvedite d '))


def Round_pi(d):
    pi = (round(math.pi // d * d, 10))
    print("pi = ", pi)

d = float(input('Введте точносить числа пи '))
Round_pi(d)


# Простые множители

def Find_prime_numbers(n):
    i = 2
    prime_numbers = []
    while n != 1:
        if n % i == 0:
            n /= i
            prime_numbers.append(i)
        else:
            i += 1
    return prime_numbers


N = int(input('Enter number '))
print(Find_prime_numbers(N))


# Не повторяющиеся числа

def Print_not_repit(list):
    for i in range(len(list)):
        if list.count(list[i]) == 1:
            print(list[i])


list = input('Введите последовтельность чисел').split()
Print_not_repit(list)

# Создание мнгочлена

def Create_polynomial(k = 3, file_name='text.txt'):
    file = open(file_name, 'w')
    for i in range(k, -1, - 1):
        c = randint(0, 100)
        if c != 0:
            if i != 0:
                file.writelines(f'{c}x^{i} + ')
            else:
                file.writelines(f'{c} ')
    file.write('= 0 ')
    file.close()


k = int(input("Enter k "))

file_name1 = "first_file.txt"
Create_polynomial(k, file_name1)

file_name2 = "second_file.txt"
Create_polynomial(3, file_name2)


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


f = open('text.txt', 'w')
f.write(Sum_poynomials(file_name1, file_name2))
f.close()


# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
#
# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой
#
# Вывод программы необходимо оформить следующим образом
# Команда:Всегоигр Побед Ничьих Поражений Всегоочков
#
# Конкретный пример ввода-вывода приведён ниже.
#
# Порядок вывода команд произвольный.
#
# Sample Input:
#
# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15
# Sample Output:
#
# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6

# список списков

def Check_team(teams, text):
    if len(teams) == 0:
        teams = {text: [0, 0, 0, 0, 0]}
    if not teams.get(text):
        teams[text] = [0, 0, 0, 0, 0]
    return teams


def Resulst(file_name = 'Footbol.txt'):
    teams = {}
    file = open(file_name, 'r', encoding='utf-8')
    text = file.readline()
    for i in range(int(text)):
        text = file.readline().split(';')
        teams = Check_team(teams, text[0])
        teams = Check_team(teams, text[2])
        teams = Match_results(teams, text)
    return teams


def Match_results(teams, text):
    teams[text[0]][0] += 1      # Участие
    teams[text[2]][0] += 1
    if text[1] > text[3]:
        teams[text[0]][1] += 1
        teams[text[2]][3] += 1
        teams[text[0]][4] += 3
    elif text[1] == text[3]:
        teams[text[0]][2] += 1
        teams[text[2]][2] += 1
        teams[text[0]][4] += 1
        teams[text[0]][4] += 1
    else:
        teams[text[0]][3] += 1
        teams[text[2]][1] += 1
        teams[text[2]][4] += 3
    return teams


print(Resulst())

