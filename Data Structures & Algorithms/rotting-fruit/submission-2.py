class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        res = 0
        queue = deque()
        visit = set()
        fresh = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    visit.add((r,c))
                    queue.append((r,c))
                if grid[r][c] == 1:
                    fresh.add((r,c))
        while queue and fresh:
            for i in range(len(queue)):
                r, c = queue.popleft()
                path = [[0,1], [1,0], [0,-1], [-1,0]]
                for dr, dc in path:
                    if min(r + dr, c + dc) < 0 or r + dr == row or c + dc == col or (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 0:
                        continue
                    visit.add((r + dr,c + dc))
                    fresh.remove((r + dr, c + dc))
                    queue.append((r + dr,c + dc))
            res += 1
        if fresh:
            return -1
        else:
            return res
