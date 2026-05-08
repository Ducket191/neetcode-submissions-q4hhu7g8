class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxsum = nums[0]
        cur = 0
        l = 0
        for r in range(len(nums)):
            if cur <= 0:
                cur = 0
                l = r
            cur += nums[r]
            maxsum = max(maxsum, cur)
        for r in range(len(nums)):
            if r == l:
                cur -= nums[l]
                l += 1
                while l < len(nums)-1 and nums[l] < 0:
                    cur -= nums[l]
                    l += 1
            cur += nums[r]
            maxsum = max(maxsum, cur)
        return maxsum
        

                
