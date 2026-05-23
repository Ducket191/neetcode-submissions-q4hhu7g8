class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        data = [nums[0], max(nums[0], nums[1])]
        i = 2
        while i < len(nums):
            c = data[1]
            data[1] = max(data[1], data[0] + nums[i])
            data[0] = c
            i += 1
        return data[1]

            