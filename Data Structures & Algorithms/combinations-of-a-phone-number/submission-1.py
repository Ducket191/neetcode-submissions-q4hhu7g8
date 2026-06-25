class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        data = {2: 'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
        res = []
        n = len(digits)
        def dfs(i, cur):
            if len(cur) == n or i > n-1:
                res.append(cur)
                return
            for item in data[int(digits[i])]:
                dfs(i+1, cur + item)
        
        dfs(0, '')
        return res