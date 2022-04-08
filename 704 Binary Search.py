class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1
        high = len(nums) - 1
        low = 0
        while high >= low:
            mid = (high + low) // 2
            if nums[mid] == target:
                res = mid
                return res
            if nums[mid] > target:
                high = mid - 1
            if nums[mid] < target:
                low = mid + 1
        return res