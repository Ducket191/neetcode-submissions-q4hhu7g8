class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r,l = 0, len(nums) - 1 
        while r < l:
            m = (l+r)//2
            if target == nums[r]:
                return r
            if target == nums[m]:
                return m
            if target == nums[l]:
                return l
            if m == r:
                break
            x = (target - nums[r]) * (target - nums[m])
            if x > 0:
                if nums[r] < nums[m]:
                    r = m
                elif nums[r] > nums[m]:
                    l = m
            elif x < 0:
                if nums[r] < nums[m]:
                    l = m
                elif nums[r] > nums[m]:
                    r = m
        if target == nums[r]:
            return r
        else:
            return -1