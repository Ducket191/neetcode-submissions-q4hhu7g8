class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        p = 1
        left = []
        right = []
        output = []
        for item in nums:
            prod = prod * item
            left.append(prod)
        for i in range(len(nums)-1, -1, -1):
            p = p * nums[i]
            right.append(p)
        for i in range (0, len(nums)):
            if i == 0:
                output.append(right[len(nums)-2])
            elif i == len(nums)-1:
                output.append(left[i-1])
            else:
                j = left[i-1] * right[len(nums)-2-i]
                output.append(j)
        return output



        
        