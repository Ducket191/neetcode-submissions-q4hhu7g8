class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [0] * n
        
        for i in range(m):
            curRow = [n] * n
            curRow[-1] = 1
            for j in range(n-2, -1, -1):
                curRow[j] = curRow[j+1] + prevRow[j]
            prevRow = curRow
        
        return prevRow[0]