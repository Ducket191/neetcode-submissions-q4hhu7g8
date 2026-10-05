class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        res = 0
        a = len(s)
        cache = {}
        
        def dfs(m,n):
            if m == n:
                return 1
            if m > n:
                return 0
            if (m,n) in cache:
                return cache[(m,n)]
            
            if s[m] == s[n]:
                cache[(m, n)] = dfs(m+1, n-1) + 2
            else:
                cache[(m, n)] = max(dfs(m+1, n), dfs(m, n-1))
            
            return cache[(m,n)]
            
        return dfs(0, a-1)