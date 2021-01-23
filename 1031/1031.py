# a = input()
# n = int(a)
# print('%o'%n)

a = int(input())
b = []
while a > 8:
    b.append(a % 8)
    a = a // 8
b.append(a)
for i in range(len(b)):
    print(b[len(b)-i-1], end='')
