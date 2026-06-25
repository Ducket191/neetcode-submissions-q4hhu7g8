class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(i, curComb):
            if len(curComb) == k:
                res.append(curComb.copy())
                return
            if i > n:
                return
            
            for j in range(i, n+1):
                curComb.append(j)
                dfs(j+1, curComb)
                curComb.pop()
            
        dfs(1, [])
        return res