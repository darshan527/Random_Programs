# https://www.codechef.com/SPYB21C/problems/VCOUPLE
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ma = 0
    mb = 0
    for i in range(n):
        ma = max(ma, a[i])
        mb = max(mb, b[i])
    print(ma + mb)
