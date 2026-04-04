import random

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        while True:
            num = random.randint(0, len(nums)-1)
            if nums.count(nums[num]) > (len(nums)/2):
                return nums[num]