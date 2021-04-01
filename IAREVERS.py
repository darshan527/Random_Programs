#https://www.codechef.com/IARCSJUD/problems/IAREVERS
n = int(input())
a = []
c = ["'",'.',',',';',':']
for _ in range(n):
    s = input()
    for i in c:
        s = s.replace(i, ' ')
    for i in s.split():
        a.append(i)
print(" ".join(reversed(a)))