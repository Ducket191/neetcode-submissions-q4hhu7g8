class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        cur = 0

        for n in nums:
            cur = max(cur, 0)
            cur += n
            maxsum = max(cur, maxsum)
        
        return maxsum
