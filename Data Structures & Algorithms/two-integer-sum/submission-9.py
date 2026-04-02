class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = defaultdict(int)
        for i in range (len(nums)):
            diff = target - nums[i]
            if diff in n and n[diff] != i:
                return [n[diff], i]
            n[nums[i]] = i
        return []