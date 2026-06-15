class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        o = []
        n = len(nums)
        freq = n // 3
        res1, res2 = None, None
        count1, count2 = 0, 0

        for num in nums:
            if num == res1:
                count1 += 1
            elif num == res2:
                count2 += 1
            elif count1 == 0:
                res1, count1 = num, 1
            elif count2 == 0:
                res2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        
        if nums.count(res1) > freq:
            o.append(res1)
        if res2 is not None and nums.count(res2) > freq:
            o.append(res2)
        return o