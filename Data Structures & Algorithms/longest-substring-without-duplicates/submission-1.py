class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = []
        if len(s) == 0:
            return 0
        res = 1
        for r in range(0, len(s)):
            seen.append(s[r])
            while len(set(seen)) != len(seen):
                l += 1
                seen.pop(0)
            if len(set(seen)) == len(seen):
                res = max(res, r - l + 1)
        return res
            