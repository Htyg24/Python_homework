# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
list = ['4', '8', 'ntheoui', 'ihcu', '11']
number = 4


def find_item(list, item):
    for i in list:
        if i == number:
            print (f'Числа {item} есть в списке')
            return
    print (f'Числа {item} нет в списке')


find_item(list, number)


# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
def Find_second_enteres(list, item):
    count = 0
    index = 0
    for i in list:
        if i == item:
            count += 1
            if count == 2:
                return index
        index += 1
    return -1


# Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве используется в этой книге.
#
# Помогите Антону написать упрощённую версию такой программы,
# которая сможет подсчитать слова, разделённые пробелом и вывести получившуюся статистику.
#
# Программа должна считывать одну строку со стандартного ввода и
# выводить для каждого уникального слова в этой строке число его повторений (без учёта регистра)
# в формате "слово количество" (см. пример вывода).
# Порядок вывода слов может быть произвольным, каждое уникальное слово должно выводиться только один раз.

list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
item = 'qwe'
print(Find_second_enteres(list, item))
line = 'a Aa abC aa ac abc bcd a'


def count_of_word(line):
    dictionary = {}
    line = line.lower()
    words = line.split()
    for item in words:
        item = item
        if item not in dictionary:
            dictionary[item] = 0
        dictionary[item] += 1
    for key, value in dictionary.items():
        print (key, value)


count_of_word(line)

print()

count_of_word("a A a")