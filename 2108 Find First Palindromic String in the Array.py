class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        res = ""
        for i in words:
            tmp = True
            j = 0
            k = len(i) - 1
            while j <= k:
                if i[j] != i[k]:
                    tmp = False
                    break
                j += 1
                k -= 1
            if tmp:
                return i
        if res == "":
            return res
