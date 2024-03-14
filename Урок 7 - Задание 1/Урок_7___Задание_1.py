string = 'искатьтакси'
pal = 'yes'

for c in range(len(string)):
    if string[c] == string[-c - 1]:
        pal = 'yes'
    else:
        pal = 'no'
        break;

print(pal);