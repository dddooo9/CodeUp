a = int(input())
b = input().split()

min_num = int(b[0])
for i in b:
    min_num = min(min_num, int(i))

print(min_num)