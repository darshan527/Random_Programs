class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            tmp = 0
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            while l < r:
                ts = nums[i] + nums[l] + nums[r]
                if ts > 0:
                    r -= 1
                elif ts < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while r > l and nums[r + 1] == nums[r]:
                        r -= 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
        return res