for _ in range(int(input())):
    n = int(input())
    ls = list(map(int, input().split()))
    odd = 0
    for i in ls:
        if i % 2 != 0:
            odd += 1
    print(odd // 2)
