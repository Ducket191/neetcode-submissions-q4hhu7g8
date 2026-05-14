class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        p = 1
        for n in nums:
            p *= n
            prefix.append(p)
        p = 1
        postfix = [1]
        for n in nums[::-1]:
            p *= n
            postfix.append(p)
        postfix.reverse()
        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * postfix[i+1])
        return res
