print('Введите пятизначное число:')
a, b, c, d, e = map(int, input())
number = float((d ** e) * c / (a - b))
print('Результат: ', number)
