class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        data = defaultdict(int)
        freq = len(nums) // 3
        res = set()
        for num in nums:
            data[num] += 1
            if data[num] > freq and not num in res:
                res.add(num)
        return list(res)