class Solution:
    def findMaximizedCapital(self, k: int, w: int, jprofits: List[int], capital: List[int]) -> int:
        res = w
        for i in range(k):
            m = 0
            c = 0
            for j in range(len(capital)):
                if capital[j] <= w:
                    if jprofits[j] == max(m, jprofits[j]):
                        m = jprofits[j]
                        c = j
            capital.pop(c)
            jprofits.pop(c)
            res += m
            w += m
        return res
            

