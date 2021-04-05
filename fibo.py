a = [0, 1]
n = int(input())
print(a[0], a[1], end=" ")
while n > 3:
    s = a[0] + a[1]
    a[0] = a[1]
    a[1] = s
    print(s, end=" ")
    n -= 1
