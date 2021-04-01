# Discrepancies in the Voters List
# https://www.codechef.com/IARCSJUD/problems/VOTERSDI
d = {}
a, b, c = list(map(int, input().split()))
for _ in range(a + b + c):
    k = int(input())
    if k in d:
        d[k] += 1
    else:
        d[k] = 1
nl = []
c = 0
for k in d.keys():
    if d[k] > 1:
        nl.append(k)
        c += 1
nl.sort()
print(c)
for i in nl:
    print(i)
