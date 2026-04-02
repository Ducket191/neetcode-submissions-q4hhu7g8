class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        prodwithout0 = 1
        output = []
        count0 = 0
        for item in nums:
            prod = prod * item
            if item == 0:
                count0 += 1
            else:
                prodwithout0 = prodwithout0 * item
        if count0 > 1:
            output2 = [0] * len(nums)
            return output2
        if count0 == 1:
            loc = nums.index(0)
        for item in nums:
            if item == 0:
                output.append(prodwithout0)
            else:
                output.append(int(prod / item))
        return output