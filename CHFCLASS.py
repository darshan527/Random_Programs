for _ in range(int(input())):
    n = int(input())
    s = n // 7
    if ((n / 7) >= (s + 0.84)):
        s += 1
    print(s)
