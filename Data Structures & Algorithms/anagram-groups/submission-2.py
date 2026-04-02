class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for item in strs:
            res["".join(sorted(item))].append(item)
        return list(res.values())
