class Solution:
        def threeSum(self, nums: List[int]) -> List[List[int]]:
                o = []
                for i in range (len(nums)):
                        target = 0 - nums[i]
                        n = nums.copy()
                        n.remove(nums[i])
                        h = []
                        for item in n:
                                item = target - item
                                h.append(item)
                        for j in range (len(n)):
                                if n[j] in (h[:j] + h[j+1:]):
                                        sor = sorted([n[j], target-n[j], nums[i]])
                                        o.append(tuple(sor))
                        output = list(set(o))
                return output

                