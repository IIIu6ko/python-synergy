print('Введите минимальную сумму инвестиций:')
min = int(input())

print('Сколько долларов у Майкла?')
mike = int(input())

print('Сколько долларов у Ивана?')
ivan = int(input())

if (mike >= min) and (ivan >= min):
    print(2)
elif mike >= min:
    print('Mike')
elif ivan >= min:
    print('Ivan')
elif mike + ivan >= min:
    print(1)
else:
    print(0)    