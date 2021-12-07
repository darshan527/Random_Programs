# https://www.codingame.com/ide/puzzle/chuck-norris
message = input()

st = ''.join(format(ord(x), '07b') for x in message)
res = []
flg = None
k = 0
while k < len(st):
    if st[k] == '1':
        tmp = '0 '
        flg = '1'
    else:
        tmp = '00 '
        flg = '0'
    while k < len(st) and st[k] == flg:
        tmp += '0'
        k += 1
    res.append(tmp)

print(*res)
