class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        row, col = len(grid), len(grid[0])
        queue = deque()
        visit = set()
        visit.add((0,0))
        queue.append((0, 0))
        res = 1
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == row - 1 and c == col - 1:
                    return res
                
                path = [[0,1], [1,0], [0,-1], [-1,0], [1,1], [-1,1], [1,-1], [-1,-1]]
                for dr, dc in path:
                    if min(r + dr, c + dc) < 0 or r + dr == row or c + dc == col or (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1:
                        continue
                    visit.add((r + dr,c + dc))
                    queue.append((r + dr,c + dc))
            res += 1
        return -1
