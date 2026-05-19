class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()
        row, col = len(grid), len(grid[0])
        res = 0
        def dfs(grid, r, c, visit):
            if r == row or c == col or min(r,c) < 0 or (r,c) in visit or grid[r][c] == 0:
                return 0
            
            visit.add((r,c))
            count = 1
            count += dfs(grid, r+1, c, visit)
            count += dfs(grid, r-1, c, visit)
            count += dfs(grid, r, c+1, visit)
            count += dfs(grid, r, c-1, visit)
            return count

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in visit:
                    x = dfs(grid, r, c, visit)
                    res = max(res, x)
        return res