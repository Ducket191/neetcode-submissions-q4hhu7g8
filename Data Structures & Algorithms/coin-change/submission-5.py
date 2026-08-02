class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        sys.setrecursionlimit(20000)
        memo = {}
        def dfs(capacity):
            if capacity == 0:
                return 0
            if capacity in memo:
                return memo[capacity]

            res = 1e9
            for coin in coins:
                newcap = capacity - coin
                if newcap >= 0:
                    res = min(res, 1 + dfs(newcap))

            memo[capacity] = res
            return res
        
        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins