class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = min(strs, key=len)
        j = 0
        while j < (len(s)):
            for i in range(len(strs)-1):
                if strs[i][j] != strs[i+1][j]:
                    return strs[0][:j]  
            j += 1
        return strs[0][:j]