# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def Comosition_sum(x):
    result = 0
    for i in range(len(x)) :
        if x[i]!= ',':
            result += int(x[i]) 
    print("-", x, "->", result)


x = input('x = ')
Comosition_sum(x)


# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.


def Factorial(x):
    multiply = 1
    result = [] 
    for i in range(1,x+1):
        multiply *= i
        result.append(multiply)
    return result


def Print_count(N):
    count = '('
    for i in range(1, N + 1):
        if i != 1:
            count += ", "
        for j in range(1, i + 1):
            count += str(j)
            if j != i:
                count += '*'
    count += ")"
    return count


N = int(input('Пусть N = '))
result = Factorial (N)
count = Print_count(N)
print("тогда", result, count)