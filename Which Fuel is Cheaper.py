for _ in range(int(input())):
    x, y, a, b, k = map(int, input().split())
    p = x + (k * a)
    d = y + (k * b)
    if p < d:
        print("DIESEL")
    elif p > d:
        print("PETROL")
    else:
        print("SAME PRICE")