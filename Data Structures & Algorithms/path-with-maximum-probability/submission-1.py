class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        count = defaultdict(list)
        for i in range(len(edges)):
            s, e = edges[i]
            count[s].append([succProb[i], e])
            count[e].append([succProb[i], s])
        
        max_probs = [0.0] * n
        max_probs[start_node] = 1.0
        maxheap = [[-1.0, start_node]]
        while maxheap:
            w, n1 = heapq.heappop(maxheap)
            w1 = -w
            if w1 < max_probs[n1]:
                continue
            if n1 == end_node:
                return w1
            for w2, n2 in count[n1]:
                if w1 * w2 > max_probs[n2]:
                    max_probs[n2] = w1 * w2
                    heapq.heappush(maxheap, [-(max_probs[n2]), n2])
        
        return 0