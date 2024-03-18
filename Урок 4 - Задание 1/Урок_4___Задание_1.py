print('Введите стороны прямоугольника, чтобы узнать его площадь и периметр:')
a, b = input().split()

if a.isdigit():
    a = int(a)
else:
    a = float(a)
    
if b.isdigit():
    b = int(b)
else:
    b = float(b)

print('Площадь прямоугольника = ', a * b)
print('Периметр прямоугольника = ', 2 * (a + b))