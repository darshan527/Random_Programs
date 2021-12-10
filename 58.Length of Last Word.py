class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        cnt = 0
        while i > -1 and s[i] == " ":
            i -= 1
        while i > -1:
            if s[i] == " ":
                break
            cnt += 1
            i -= 1
        return cnt