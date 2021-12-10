from functools import reduce
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    x = 0
    res = -1
    while res != 0:
        res = reduce(lambda x, y: x ^ y, a)