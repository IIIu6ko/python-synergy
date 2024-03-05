n = int(input())
zero = 0
while n > 0:
    num = int(input())
    if num == 0:
        zero += 1
    n -= 1
        
print(zero)