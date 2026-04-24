class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        def check(n: int):
            count = 0
            for item in piles:
                count += math.ceil(item / n)
            if count > h:
                return True
            elif count <= h:
                return False
        l, r = 1, res
        while l <= r:
            m = (l+r)//2
            if check(m):
                l = m+1
            else:
                res = m
                r = m-1
        return res