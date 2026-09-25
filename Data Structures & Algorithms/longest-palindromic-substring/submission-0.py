class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = ""
        n = len(s)
        for i in range(n):
            l,r = i,i
            while l >= 0 and r <= n-1 and s[l] == s[r]:
                if (r-l+1) > len(length):
                    length = s[l:r+1]
                l -= 1
                r += 1
            
            l, r = i, i+1
            while l >= 0 and r <= n-1 and s[l] == s[r]:
                if (r-l+1) > len(length):
                    length = s[l:r+1]
                l -= 1
                r += 1
            
        return length