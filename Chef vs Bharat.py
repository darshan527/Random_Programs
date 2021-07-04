# n = int(input())
# ln = len(n)


def chefora(s):
    # tmp = 0
    # for i in range(len(s)):
    #     tmp += (int(s[i]) * (10**i))
    # print(tmp)
    # if str(tmp) == s:
    #     return True
    # else:
    #     return False

    if len(s) % 2 != 0:
        x = len(s) // 2
        print(x)
        x1 = list(s[x:])
        x1.reverse()
        print(x1, s[:x + 1])
        if x1 == s[:x + 1]:
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    n = input()
    print(chefora(n))