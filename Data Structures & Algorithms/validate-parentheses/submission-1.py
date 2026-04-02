class Solution:
    def isValid(self, s: str) -> bool:
        while len(s) > 0:
            if '{}' in s or '[]' in s or '()' in s:
                s = s.replace('()','')
                s = s.replace('{}','')
                s = s.replace('[]','')
            else:
                return False
        return True