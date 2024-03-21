line = list(map(int, input().split()))
yes = set()

for i in line:
    if i in yes:
        print(i, '- YES')
    else:
        print(i, '- NO')
        yes.add(i)