print('Введите любое число:')
number = int(input())


if (number > 0) and (number % 2 == 0):
    print('Это чётное положительное число')
elif (number > 0) and (number % 2 != 0):
    print('Это нечётное положительное число')
elif (number < 0) and (number % 2 == 0):
    print('Это чётное отрицательное число')
elif (number < 0) and (number % 2 != 0):
    print('Это нечётное отричательное число')
else:
    print('Это нулевое число')

"""
if number > 0:
    if number % 2 == 0:
        print('Это чётное положительное число')
    else:
        print('Это нечётное положительное число')    
elif number < 0:
    if number % 2 == 0:
        print('Это чётное отрицательное число')
    else:
        print('Это нечётное отрицательное число')
else:
    print('Это нулевое число')
"""