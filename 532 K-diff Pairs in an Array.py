class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        tmp = set()
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                ni = nums[i]
                nj = nums[j]
                if nj > ni:
                    t = nj
                    nj = ni
                    ni = t
                if abs(ni - nj) == k and ((ni, nj) not in tmp):
                    res += 1
                    tmp.add((ni, nj))
        return res