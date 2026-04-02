class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        i = 0
        c = 0
        for i in nums:
            if i == 1:
                c += 1
            else:
                c = 0
            res = max(res, c)
        return res