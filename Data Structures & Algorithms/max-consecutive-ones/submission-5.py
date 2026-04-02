class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, total = 0, 0 
        for num in nums:
            if num == 1:
                count +=1
            else:
                if count > total:
                    total = count
                count = 0
        if count > total:
            total = count
        return total
