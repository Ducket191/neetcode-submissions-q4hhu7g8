class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visit = {}
        res = 0
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []

        for s, d, w in times:
            adj[s].append([d, w])

        minheap = [[0, k]]
        while minheap:
            cost, node = heapq.heappop(minheap)
            if node in visit:
                continue
            visit[node] = cost
            res = max(res, cost)
            for n2, w2 in adj[node]:
                if n2 not in visit:
                    heapq.heappush(minheap, [cost+w2, n2])
        if len(visit) == n:
            return res
        else:
            return -1
            
            