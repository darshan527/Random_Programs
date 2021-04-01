# https://www.codechef.com/IARCSJUD/problems/IAREVERS
n = int(input())
a = []
c = ["'", ".", ",", ";", ":"]
for _ in range(n):
    s = input()
    for i in c:
        s = s.replace(i, " ")
    a.append(s)
for i in reversed(a):
    print(" ".join(reversed(i.split())))
