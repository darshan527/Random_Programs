for _ in range(int(input())):
    x, y = map(int, input().split())
    if (x + (2 * y)) % 2 == 0:
        print("Yes")
    else:
        print("No")