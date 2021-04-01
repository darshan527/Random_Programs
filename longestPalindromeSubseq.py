def longestPalindrome(s, length):
    currentLongest = [0, 1]
    for i in range(1, len(s)):
        odd = checkPalindrome(s, i - 1, i + 1, length)
        even = checkPalindrome(s, i - 1, i, length)
        longest = max(odd, even, key=lambda x: x[1] - x[0])
        currentLongest = max(longest,
                             currentLongest,
                             key=lambda x: x[1] - x[0])
    print(currentLongest[1] - currentLongest[0])
    print(s[currentLongest[0]:currentLongest[1]])


def checkPalindrome(s, l, r, length):
    while l >= 0 and r < length:
        if s[l] != s[r]:
            break
        l -= 1
        r += 1
    return [l + 1, r]


if __name__ == "__main__":
    n = int(input())
    s = input()
    longestPalindrome(s, n)
