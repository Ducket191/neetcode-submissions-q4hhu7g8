class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for c in s:
            d1[c] += 1
        for c in t:
            d2[c] += 1
        if d1 == d2:
            return True
        else:
            return False