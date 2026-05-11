class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        n = nums[0]
        res = 1
        for r in range(1, len(nums)):
            if not nums[r] <= n:
                nums[l] = nums[r]
                l += 1
                res += 1
                n = nums[r]
        return res