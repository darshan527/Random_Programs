m = 15746
n = int(input())
a, b = 0, 1
for i in range(n):
    a, b = b % m, (a + b) % m
print(b)
