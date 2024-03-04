print('Введите любое слово маленькими латинскими буквами и я вам отвечу сколько там согласных и гласных букв')

letters = list(input())
vowels = 0
consonant = 0
a = False
e = False
i = False
o = False
u = False

for x in letters:
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
        vowels += 1
        if x == 'a':
            a += 1
        elif x == 'e':
            e += 1
        elif x == 'i':
            i += 1
        elif x == 'o':
            o += 1
        elif x == 'u':
            u += 1
    else:
        consonant += 1
        
print('Гласных:', vowels, 'Согласных:', consonant)
print('Количество каждой из гласных букв:')
print('a -', a)
print('e -', e)
print('i -', i)
print('o -', o)
print('u -', u)
