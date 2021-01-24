a, b, c = input().split()
print(int(c) if (int(b) if int(a) > int(b) else int(a)) > int(c) else (int(b) if int(a) > int(b) else int(a)))