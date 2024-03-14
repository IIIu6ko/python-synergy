string = 'Мы       любим        животных и стараемся     поддерживать тех      из  них, кому     не посчастливилось иметь ласковых        хозяев и тёплый кров.'
spaces = ''
spacesArr = []

for c in range(len(string)):
    if string[c] == ' ':
        spaces += string[c]
    else:
        if len(spaces) > 1:
            spacesArr.append(spaces)
        spaces = ''

for spaces in spacesArr:
    stringArr = string.split(spaces, 1)
    string = ' '.join(stringArr)

print(string)


    
