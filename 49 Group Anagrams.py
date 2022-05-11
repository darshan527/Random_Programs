class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tmp_dict = {}
        for i in strs:
            x = "".join(sorted(i))
            if x in tmp_dict:
                tmp_dict[x].append(i)
            else:
                tmp_dict[x] = [i]

        return [i for i in tmp_dict.values()]