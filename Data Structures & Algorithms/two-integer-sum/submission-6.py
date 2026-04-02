class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        n = []
        for num in nums:
            n.append(target - num)
        for i in range(len(nums)):
            if nums[i] in (n[:i] + n[i+1:]):
                res.append(i)
        return res