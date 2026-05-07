class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        data = []
        heapq.heapify(data)
        for n in nums:
            heapq.heappush(data, n)
            if len(data) > k:
                heapq.heappop(data)
        return data[0]
