class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        minheap = [[grid[0][0], 0, 0]]
        neighbour = [[0,1], [1,0], [0,-1], [-1,0]]

        visit.add((0,0))
        while minheap:
            w, r, c = heapq.heappop(minheap)
            if r == N-1 and c == N-1:
                return w

            for dr, dc in neighbour:
                if (min(r + dr, c + dc) < 0 or
                    r + dr == N or c + dc == N or
                    (r + dr, c + dc) in visit):
                    continue
                visit.add((r+dr, c+dc))
                heapq.heappush(minheap, [max(w, grid[r+dr][c+dc]), r+dr, c+dc])