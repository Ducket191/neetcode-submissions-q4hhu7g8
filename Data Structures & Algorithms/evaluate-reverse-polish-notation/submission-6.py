class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if item in {"+", "-", "*", "/"}:
                x = stack.pop()
                y = stack.pop()
                if item == "+":
                    stack.append(x+y)
                elif item == "-":
                    stack.append(y-x)
                elif item == "*":
                    stack.append(x*y)
                elif item == "/":
                    stack.append(int(y / x))
            else:
                stack.append(int(item))
        return stack[0]