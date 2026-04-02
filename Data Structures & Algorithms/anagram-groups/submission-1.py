class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            groups[tuple(sorted(s))].append(s)
        return list(groups.values())