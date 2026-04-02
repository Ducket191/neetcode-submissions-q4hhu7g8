class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        n = defaultdict(int)
        for i in range (len(nums)):
            n[nums[i]] = i
        for i in range (len(nums)):
            diff = target - nums[i]
            if diff in n and n[diff] != i:
                return [i, n[diff]]
        return []