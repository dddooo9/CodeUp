a = input()
for i in range(1, 16):
    i = hex(i)[2:]
    mt = hex(int(a, 16) * int(i, 16))[2:]
    print("{0}*{1}={2}".format(a, i.upper(), mt.upper()))