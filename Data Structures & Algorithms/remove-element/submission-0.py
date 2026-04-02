class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = 0
        k = []
        for num in nums:
            if num != val:
                k.append(num)
        for i in range(len(k)):
            nums[i] = k[i]   
        return len(k)