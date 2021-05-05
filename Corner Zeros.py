a = [0, 1, 3, 0, 2]
# a = [0, 0]


def cornerZeros(a):
    zpos = 0
    l = len(a)
    for k in range(l):
        if a[k] == 0:
            zpos = k
        if a[k] != 0:
            # tmp = a[zpos]
            a[zpos] = a[k]
            a[k] = 0
    return a


res = cornerZeros(a)
print(res)