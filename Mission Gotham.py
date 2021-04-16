# https://www.codechef.com/SPYB21C/problems/GOTHAM
n = int(input())
arr = list(map(int, input().split()))
for i in range(int(input())):
    x, k = list(map(int, input().split()))
    t = 0
    while k > 0 and x < n:
        pass