a = int(input())
b = int(input())
string = ''

for i in range(a, b + 1):
    if i % 2 == 0:
        string += str(i) + ' '

print(string)
