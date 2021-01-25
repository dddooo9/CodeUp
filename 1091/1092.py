a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
max_num = max(a, b, c)
while max_num % a != 0 or max_num % b != 0 or max_num % c != 0:
    max_num += 1
print(max_num)