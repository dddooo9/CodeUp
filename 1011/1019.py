num = input()
a = num.split(".")
print("{0:04d}.{1:02d}.{2:02d}".format(int(a[0]), int(a[1]), int(a[2])))