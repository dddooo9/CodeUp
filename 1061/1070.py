a = int(input())
if a % 12 < 3:
    print("winter")
elif a % 12 < 6:
    print("spring")
elif a % 12 < 9:
    print("summer")
else:
    print("fall")