class Solution:
    def climbStairs(self, n: int) -> int:
        pp = 1
        p = 2
        if n == 1:
            return pp
        if n == 2:
            return p
        for _ in range(3,n+1):
            c = p
            p = p + pp
            pp = c
        return p