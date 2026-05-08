class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s = 0
        L = 0
        res = float("inf")
        for R in range (len(nums)):
            s += nums[R]
            while s >= target:
                res = min(res, R-L+1)
                s -= nums[L]
                L += 1
    
        if res > len(nums):
            return 0
        else:
            return res