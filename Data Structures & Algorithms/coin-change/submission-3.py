class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        sys.setrecursionlimit(20000)
        M, N = len(coins), amount + 1
        dp = [[-2]*N for _ in range(M)]
        def dfs(i, capacity):
            if capacity == 0:
                return 0
            if i == M:
                return float('inf')
            if dp[i][capacity] != -2:
                return dp[i][capacity]

            res = dfs(i+1, capacity)

            new = capacity - coins[i]
            if new >= 0:
                c = 1 + dfs(i, new)
                res = min(c, res)

            dp[i][capacity] = res
            return res
        
        ans = dfs(0, amount)
        return ans if ans != float('inf') else -1