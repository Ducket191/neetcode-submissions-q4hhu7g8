class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = []
        for item in matrix:
            total = 0
            tmp = [0]
            for n in item:
                total += n
                tmp.append(total)
            self.prefix.append(tmp)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for i in range(row1, row2+1):
            r = self.prefix[i][col2 + 1]
            l = self.prefix[i][col1]
            res += r - l
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)