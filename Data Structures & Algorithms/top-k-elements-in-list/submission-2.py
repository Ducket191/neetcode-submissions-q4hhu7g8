class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        v = dict(sorted(count.items(), key=lambda x: x[1]))
        r = list(v.keys())
        res = []
        for i in range(len(r)-1,len(r)-1-k,-1):
            res.append(r[i])
        return res
