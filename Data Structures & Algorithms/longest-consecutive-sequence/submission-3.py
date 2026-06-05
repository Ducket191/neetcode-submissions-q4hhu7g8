class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        res = 0
        for i in nums:
            if not i-1 in n:
                a = i
                tmpt = 1
                while a + 1 in n:
                    tmpt += 1
                    a += 1
                res = max(res, tmpt)
        
        return res
