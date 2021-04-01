# https://www.codechef.com/IARCSJUD/problems/ENDCORR
from heapq import heappush, heappop

arr = []
killed = []
n, v = list(map(int, input().split()))
for _ in range(n + v):
    k = int(input())
    if k == -1:
        killed.append(heappop(arr))
        continue
    heappush(arr, -k)
for i in killed:
    print(i * -1)
