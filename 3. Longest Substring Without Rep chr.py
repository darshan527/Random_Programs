class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tmp = {}
        l, r = 0, 0
        res = 0
        while r < len(s):
            if s[r] in tmp and tmp[s[r]] >= l:
                l = tmp[s[r]] + 1

            res = max(res, r - l + 1)
            tmp[s[r]] = r
            r += 1
        return res