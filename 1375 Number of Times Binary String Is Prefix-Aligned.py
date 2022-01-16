class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        mx = 0
        pa = 0
        for i in range(len(flips)):
            if flips[i] > mx:
                mx = flips[i]
            if mx == i + 1:
                pa += 1
        return pa