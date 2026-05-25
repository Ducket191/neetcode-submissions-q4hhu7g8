class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ltext1 = len(text1)
        ltext2 = len(text2)
        cache = {}

        def dfs(t1, t2):
            if t1 == ltext1 or t2 == ltext2:
                return 0
            if (t1, t2) in cache:
                return cache[(t1, t2)]

            if text1[t1] == text2[t2]:
                cache[(t1, t2)] = 1 + dfs(t1 + 1, t2 + 1)
            else:
                cache[(t1, t2)] = max(dfs(t1 + 1, t2), dfs(t1, t2 + 1))

            return cache[(t1, t2)]

        return dfs(0, 0)