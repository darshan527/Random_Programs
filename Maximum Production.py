# https://www.codechef.com/JULY21C/problems/EITA

for _ in range(int(input())):
    d, x, y, z = list(map(int, input().split()))
    a = (x * 7)
    b = ((y * d) + ((7 - d) * z))
    if a > b:
        print(a)
    else:
        print(b)
