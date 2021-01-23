# a = input()
# n = int(a, 8)
# print(n)

a = input()
sum = 0
for i in range(len(a)):
    sum += int(a[len(a)-i-1]) * (8**i)
print(sum)