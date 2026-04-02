class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        contain = []
        for i in range(len(nums)):
            if nums[i] not in contain:
                contain.append(nums[i])
            else:
                return True
        return False