dm = []
for i in range(19):
    dm.append(input().split())

n = int(input())

for i in range(n):
    a = input().split()
    for j in range(19):
        if dm[int(a[0]) - 1][j] == '0':
            dm[int(a[0]) - 1][j] = '1'
        else:
            dm[int(a[0]) - 1][j] = '0'

        if dm[j][int(a[1]) - 1] == '0':
            dm[j][int(a[1]) - 1] = '1'
        else:
            dm[j][int(a[1]) - 1] = '0'

for i in range(19):
    for j in range(19):
        print(dm[i][j], end=' ')
    print()