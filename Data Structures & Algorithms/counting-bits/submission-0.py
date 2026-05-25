class Solution:
    def countBits(self, n: int) -> List[int]:
        def count(n):
            res = 0
            while n > 0:
                if n & 1 == 1:
                    res += 1
                n >>= 1
            return res
        op = []
        for i in range(n + 1):
            op.append(count(i))
        
        return op