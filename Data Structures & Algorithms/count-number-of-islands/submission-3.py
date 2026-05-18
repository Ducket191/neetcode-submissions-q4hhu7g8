class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        res = 0
        def dfs(grid, r, c, visit):
            row, col = len(grid), len(grid[0])
            if r == row or c == col or min(r,c) < 0 or (r,c) in visit or int(grid[r][c]) == 0:
                return

            visit.add((r,c))
            seen.add((r,c))
            dfs(grid, r+1, c, visit)
            dfs(grid, r-1, c, visit)
            dfs(grid, r, c+1, visit)
            dfs(grid, r, c-1, visit)
            # no visit.remove((r,c)) as we dont need to find all paths but just the clust of '1'
            return
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if int(grid[r][c]) == 1 and not (r,c) in seen:
                    dfs(grid, r, c, seen)
                    res += 1  
        return res