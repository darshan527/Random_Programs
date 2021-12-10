for _ in range(int(input())):
    x, y = map(int, input().split())
    if x == 0 and y % 2 == 0:
        print("Yes")
    elif x == 0 and y % 2 != 0:
        print("No")
    elif (x + (2 * y)) % 2 == 0:
        print("Yes")
    else:
        print("No")