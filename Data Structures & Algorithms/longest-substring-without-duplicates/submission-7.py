class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = set()
        l = 0
        if not s:
            return 0
        res = 1
        
        for r in range(len(s)):
            if s[r] in c:
                res = max(r-l, res)
                while s[r] in c:
                    c.remove(s[l])
                    l += 1
            c.add(s[r])
            res = max(r-l+1, res)
        
        return res
            
