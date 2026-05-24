class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row, col = len(obstacleGrid), len(obstacleGrid[0])

        def dfs(r, c, cache):
            if r == row or c == col or obstacleGrid[r][c] == 1:
                return 0
            if cache[r][c] > 0:
                return cache[r][c]
            if r == row - 1 and c == col - 1:
                return 1
            
            cache[r][c] = (dfs(r+1, c, cache) + dfs(r, c+1, cache))
            return cache[r][c]
        
        return dfs(0, 0, [[0] * col for i in range(row)])
