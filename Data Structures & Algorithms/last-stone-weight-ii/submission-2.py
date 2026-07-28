class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        res = 0
        cache = {}
        def dfs(i, s):
            if i == n:
                return s
            if (i,s) in cache:
                return cache[(i,s)]
            
            cache[(i,s)] = min(abs(dfs(i+1, s + stones[i])), abs(dfs(i+1, s - stones[i])))
            return cache[(i,s)]
        
        return dfs(0, 0)