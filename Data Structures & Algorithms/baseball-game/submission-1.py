class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        s = 0
        for item in operations:
            if item == '+':
                s += res[-1]+res[-2]
                res.append(res[-1]+res[-2])
            elif item == 'D':
                s += (res[-1] * 2)
                res.append(res[-1] * 2)
            elif item == 'C':
                s -= res[-1]
                res.pop()
            else:
                s += int(item)
                res.append(int(item))
        return s