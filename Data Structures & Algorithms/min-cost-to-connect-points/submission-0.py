class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minheap = [[0, points[0][0], points[0][1]]]
        visit = set()
        n = len(points)
        res = 0
        while len(visit) < n:
            w, x, y = heapq.heappop(minheap)
            if (x,y) in visit:
                continue
            visit.add((x,y))
            res += w
            for x1, y1 in points:
                if [x1, y1] == [x,y] or (x1, y1) in visit:
                    continue
                heapq.heappush(minheap, [abs(x-x1)+abs(y-y1), x1, y1])
        
        return res