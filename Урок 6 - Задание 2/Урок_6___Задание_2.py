num = int(input())
dividers = 0

for i in range(num + 1, 0, -1):
    if num % i == 0:
        dividers += 1
        
print(dividers)