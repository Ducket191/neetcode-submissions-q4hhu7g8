class Solution:
    def findMin(self, nums: List[int]) -> int:
        while len(nums) > 2:
            if nums[0] < nums[-1]:
                return nums[0]
            else:
                i = len(nums) // 2
                if nums[0] > nums[i]:
                    nums = nums[:i+1]
                else:
                    nums = nums[i+1:]
        if len(nums) == 1:
            return nums[0]
        else:
            return min(nums)
                
        