class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        sorted_dict = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))
        return list(sorted_dict.keys())[:k]
        
        
            
        
        