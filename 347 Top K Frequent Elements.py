class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        tmp = [[] for _ in range(len(nums) + 1)]

        for i in nums:
            cnt[i] = 1 + cnt.get(i, 0)

        for i, j in cnt.items():
            tmp[j].append(i)

        res = []
        print(tmp, cnt)
        for i in range(len(tmp) - 1, 0, -1):
            for j in tmp[i]:
                print(j)
                res.append(j)
                if len(res) == k:
                    return res
