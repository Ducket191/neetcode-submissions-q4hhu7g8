class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        res, n = [], len(nums)
        perm = []
        def dfs():
            if len(perm) == n:
                res.append(perm.copy())
            
            for num in count:
                if count[num] > 0:
                    perm.append(num)
                    count[num] -= 1
                    dfs()
                    perm.pop()
                    count[num] += 1
        
        dfs()
        return res
            