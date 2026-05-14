class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        p = 1
        for n in nums:
            res.append(p)
            p *= n
    
        p = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= p
            p *= nums[i]
        return res
