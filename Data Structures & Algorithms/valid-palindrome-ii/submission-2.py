class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(s):
            l, r = 0, len(s)-1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return check(s[l:r]) or check(s[l+1:r+1])
            else:
                l += 1
                r -= 1 
        return True