w, h, b = input().split()
print("%.2f" % (int(w) * int(h) * int(b)) / (8 * 1024 * 1024), "MB")