class MinStack:

    def __init__(self):
        self.m = float("inf")
        self.checkm = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.m = min(val, self.m)
        self.checkm.append(self.m)

    def pop(self) -> None:
        self.stack.pop()
        self.checkm.pop()
        if self.checkm:
            self.m = self.checkm[-1]
        else:
            self.m = float("inf")

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.checkm[-1]
        
