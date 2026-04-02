class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = []
        c = 0
        for i in nums:
            if i == 1:
                c += 1
            else:
                res.append(c)
                c = 0
        res.append(c)
        return max(res)