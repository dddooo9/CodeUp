a = input()
n = len(a)
for i in range(n):
    print("[{0}]".format(int(a[i]) * 10 ** (n-i-1)))