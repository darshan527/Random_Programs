# https://www.codechef.com/SPYB21C/problems/VCOUPLE
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort(reverse=True)
    m = 0
    for i in range(n):
        m = max(m, a[i] + b[i])
    print(m)
