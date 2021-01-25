h = []
for i in range(10):
    b = input().split()
    h.append([])
    for j in range(10):
        h[i].append(int(b[j]))

ant_x = 1
ant_y = 1

while True:
    if h[ant_x][ant_y] == 2 or (h[ant_x][ant_y + 1] == 1 and h[ant_x + 1][ant_y] == 1):
        h[ant_x][ant_y] = 9
        break
    h[ant_x][ant_y] = 9
    if h[ant_x][ant_y + 1] == 1:
        ant_x += 1
    else:
        ant_y += 1

for i in range(10):
    for j in range(10):
        print(h[i][j], end=' ')
    print()