class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        res = m = 0

        for num in nums:
            count[num] += 1
            if count[num] > m:
                m = count[num]
                res = num
        return res