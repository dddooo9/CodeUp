a = input()
a = a.split()
for i in range(len(a)):
    if int(a[i]) % 2 == 0:
        print(int(a[i]))
