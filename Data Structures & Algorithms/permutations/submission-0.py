class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(i):
            if i == len(nums):
                return [[]]
            res = []
            perm = dfs(i+1)
            for p in perm:
                for j in range(len(p) + 1):
                    pc = p.copy()
                    pc.insert(j, nums[i])
                    res.append(pc)

            return res
        return dfs(0)