class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums) - 1
            a = nums[i]
            while l < r:
                S = a + nums[r] + nums[l]
                if S > 0:
                    r -= 1
                elif S < 0:
                    l += 1
                elif S == 0:
                    res.append([a, nums[r], nums[l]])
                    r,l = r-1, l+1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res