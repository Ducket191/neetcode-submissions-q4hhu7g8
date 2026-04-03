class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums)
        i = nums[0]
        count = res = 0
        for item in nums:
            if item == i:
                count += 1
                if count > len(nums) // 2:
                    return item
            else:
                res = max(res, count)
                i = item
                count = 1
        return nums[-1]
