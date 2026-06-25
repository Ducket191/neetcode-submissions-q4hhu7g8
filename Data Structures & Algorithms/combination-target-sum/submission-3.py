class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(i, total, curComb):
            if total == target:
                res.append(curComb.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            curComb.append(nums[i])
            dfs(i, total + nums[i], curComb)
            curComb.pop()
            dfs(i+1, total, curComb)
        
        dfs(0,0,[])
        return res
            
