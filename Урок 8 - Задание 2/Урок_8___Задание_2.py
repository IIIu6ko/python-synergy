def arrChange(arr):
    arr.insert(0, arr[-1])
    arr.pop()
    
    return arr
        
n = int(input())
l = list(map(int, input().split()))[:n]

print(arrChange(l))