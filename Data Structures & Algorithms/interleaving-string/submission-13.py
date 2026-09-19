class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        a,b,c = len(s1), len(s2), len(s3)
        if a + b != c:
            return False

        dp = {}
        def dfs(m,n,q):
            if q == c:
                return (m == a) and (n == b)
            if (m,n) in dp:
                return dp[(m,n)]

            res = False
            if m < a and s3[q] == s1[m]:
                res = dfs(m+1,n,q+1)
            if not res and n < b and s3[q] == s2[n]:
                res = dfs(m,n+1,q+1)

            dp[(m,n)] = res
            return res

        return dfs(0,0,0)
        
        
        
        

            
            
