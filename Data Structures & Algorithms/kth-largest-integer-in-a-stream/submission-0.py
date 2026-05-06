class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.data = sorted(nums)
        self.k = k

    def add(self, val: int) -> int:
        self.data.append(val)
        self.data.sort()
        return self.data[-self.k]

        
