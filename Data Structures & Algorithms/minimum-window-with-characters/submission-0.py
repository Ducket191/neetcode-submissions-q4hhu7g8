class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        c = defaultdict(int)
        n = defaultdict(int)
        for item in t:
            n[item] += 1
            c[item] = 0
        minr = len(s)
        res = ""
        cur = ""
        l = 0
        for r in range(len(s)):
            cur += s[r]
            if s[r] in t:
                c[s[r]] += 1

            while all(c[k] >= n[k] for k in n):
                minr = min(minr, r-l+1)
                if len(cur) <= minr:
                    res = cur
                cur = cur[1:]
                if s[l] in t:
                    c[s[l]] -= 1
                l += 1
        return res
            