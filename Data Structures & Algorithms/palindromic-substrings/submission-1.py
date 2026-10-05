class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        a = len(s)

        for i in range(a):
            m,n = i, i
            while m >= 0 and n <= a-1 and s[m] == s[n]:
                res += 1
                m -= 1
                n += 1

            m,n = i, i+1
            while m >= 0 and n <= a-1 and s[m] == s[n]:
                m -= 1
                n += 1
                res += 1

        return res