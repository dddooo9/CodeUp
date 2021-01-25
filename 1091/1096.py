dm = [[0 for i in range(19)] for i in range(19)]

n = int(input())
for i in range(n):
    x, y = input().split()
    dm[int(x) - 1][int(y) - 1] = 1

for i in range(len(dm)):
    for j in range(len(dm[i])):
        print(dm[i][j], end=' ')
    print()


