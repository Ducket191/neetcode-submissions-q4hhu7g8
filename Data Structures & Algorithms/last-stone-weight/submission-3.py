class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        data = []
        heapq.heapify(data)
        for item in stones:
            heapq.heappush(data, -item)
        while len(data) > 1:
            cur = heapq.heappop(data) - heapq.heappop(data)
            if cur:
                heapq.heappush(data, cur)
        if data:
            return -data[0]
        else:
            return 0