n = int(input())
arr = []

if (n > 1) and (n < 10000):
    for i in range(n):
        num = int(input())
        if num < 10e5:
            arr.append(num)

arr.reverse()
print(arr)
