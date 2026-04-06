class Solution:
    def isValid(self, s: str) -> bool:
        check = {')':'(', ']':'[', '}':'{'}
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if not stack:
                    return False
                o = stack.pop()
                if check[c] != o:
                    return False
        return not stack