class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = ""
        for i in s:
            if i.isalnum():
                tmp += i.lower()
        l = 0
        r = len(tmp) - 1
        while l <= r:
            if tmp[l] != tmp[r]:
                return False
            l += 1
            r -= 1
        return True
