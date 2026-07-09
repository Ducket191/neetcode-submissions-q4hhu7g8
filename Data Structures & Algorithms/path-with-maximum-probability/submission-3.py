class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        count = defaultdict(list)
        for i in range(len(edges)):
            s, e = edges[i]
            count[s].append([succProb[i], e])
            count[e].append([succProb[i], s])
        
        maxheap = [[-1, start_node]]
        visit = set()
        while maxheap:
            w1, n1 = heapq.heappop(maxheap)
            visit.add(n1)

            if n1 == end_node:
                return -w1

            for w2, n2 in count[n1]:
                if n2 in visit:
                    continue
                heapq.heappush(maxheap, [w1 * w2, n2])
        
        return 0