class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0, len(matrix)-1
        while l <= r:
            m = (l+r)//2
            i,j = 0, len(matrix[m])-1
            while i <= j:
                m1 = (i+j)//2
                if target < matrix[m][m1]:
                    j = m1 - 1
                elif target > matrix[m][m1]:
                    i = m1 + 1
                else:
                    return True
            if target < matrix[m][0]:
                r = m - 1
            elif target > matrix[m][0]:
                l = m + 1
        return False
            