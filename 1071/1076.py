a = input()
b = 'a'
while True:
    print(b, end = ' ')
    b = chr(ord(b) + 1)
    if b > a:
        break