for _ in range(int(input())):
    s = input()
    px = s[0]
    sx = s[-1]
    mx = -1
    cnt = 0
    for i in s:
        if i == px or i == sx:
            cnt = 0
        else:
            cnt += 1
            mx = max(cnt, mx)
    print(mx)