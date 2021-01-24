a = input()
a = a.split()
for i in range(len(a)):
    if int(a[i]) % 2 == 0:
        print("even")
    else:
        print("odd")
