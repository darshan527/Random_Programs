#https://www.codechef.com/SPYB21C/problems/SAVWATER
for _ in range(int(input())):
    c, x, y, h = list(map(int, input().split()))
    if ((x + (y // 2)) * c) <= h:
        print("YES")
    else:
        print("NO")
