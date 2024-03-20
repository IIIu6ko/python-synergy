m = int(input())
n = int(input())
w = 0

for i in range(n):
    w += int(input())
    
print(-(-w // m))
