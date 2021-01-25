a = int(input())
b = input().split()
call = [0] * 24
for i in range(len(b)):
    call[int(b[i])] += 1


for i in range(1, 24):
    print(call[i], end=' ')

