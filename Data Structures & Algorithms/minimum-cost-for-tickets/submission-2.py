class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}
        n = len(days)

        def dfs(i):
            if i == n:
                return 0
            
            if i in dp:
                return dp[i]
            
            dp[i] = float("inf")
            dp[i] = min(dp[i], costs[0] + dfs(i+1))

            j = i
            while j < n and days[j] < days[i] + 7:
                j += 1
            dp[i] = min(dp[i], costs[1] + dfs(j))

            k = i
            while k < n and days[k] < days[i] + 30:
                k += 1
            dp[i] = min(dp[i], costs[2] + dfs(k))
        
            return dp[i]
        
        return dfs(0)