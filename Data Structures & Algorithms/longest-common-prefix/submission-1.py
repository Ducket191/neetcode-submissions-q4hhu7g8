class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        x = strs[0]
        for item in strs:
            x = self.search(x, item)
        return x


    def search(self, s1: str, s2: str):
        x = ''
        for i in range(min(len(s1), len(s2))):
            if s1[i] == s2[i]:
                x += s2[i]
            else:
                return x
        return x
            
                
                    