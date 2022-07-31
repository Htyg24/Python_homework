def day_of_week(day):
    if 1 <= day <= 5:
        print('This day a weekday(')
    elif 6 <= day <= 7:
        print('This day a weekend)')
    else:
        print('U entered a wrong number!')
    input()
def quarter(x, y):
    if x > 0 and y > 0:
        print('This point in first quarter')
    elif x < 0 and y > 0:
        print('This point in second quarter')
    elif x < 0 and y < 0:
        print('This point in third quarter')
    else:
        print('This point in fourth quarter')
    input()
day = int(input('Enter day number '))
day_of_week(day)
x = int(input('Enter X '))
y = int(input('Enter Y '))
quarter(x, y)





