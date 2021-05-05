# a = [0, 1, 3, 0, 2]
a = [0, 0]


def cornerZeros(a):
    i = 0
    j = 0
    l = len(a)
    while i < l and j < l:
        while i < l and a[i] != 0:
            i += 1
        j = i + 1
        while j < l and a[j] == 0:
            j += 1
            if i >= l or j >= l:
                return a
            else:
                tmp = a[i]
                a[i] = a[j]
                a[j] = tmp
        # print(i, j, a)
        i += 1
        j += 1
    return a


res = cornerZeros(a)
print(res)