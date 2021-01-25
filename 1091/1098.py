w, h = input().split()
w = int(w)
h = int(h)
dm = []
for i in range(w):
    dm.append([])
    for j in range(h):
        dm[i].append(0)

n = int(input())
for i in range(n):
    a = input().split()
    length = int(a[0])
    d = int(a[1])
    x = int(a[2]) - 1
    y = int(a[3]) - 1

    if d == 0:
        for j in range(y, y + length):
            dm[x][j] = 1
    else:
        for j in range(x, x + length):
            dm[j][y] = 1

for i in range(w):
    for j in range(h):
        print(dm[i][j], end=' ')
    print()
