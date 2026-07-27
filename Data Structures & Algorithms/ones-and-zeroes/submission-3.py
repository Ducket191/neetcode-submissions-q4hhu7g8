class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cache = {}
        s = len(strs)
        def dfs(i, m, n):
            if i == s:
                return 0
            if m == 0 and n == 0:
                return 0
            if (i, m, n) in cache:
                return cache[(i, m, n)]
            
            
            res = dfs(i+1, m, n)
            tm, tn = m, n
            for c in strs[i]:
                if int(c) == 0:
                    tm -=1
                else:
                    tn -= 1
            if tm >= 0 and tn >= 0:
                res = max(res, 1 + dfs(i + 1, tm, tn))

            cache[(i, m, n)] = res
            return res
        
        return dfs(0, m, n)
