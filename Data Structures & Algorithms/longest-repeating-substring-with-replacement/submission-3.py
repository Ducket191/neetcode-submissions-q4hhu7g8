class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 1
        cur = []
        for r in range(len(s)):
            cur.append(s[r])
            while not self.isValid(cur, k):
                l += 1
                cur.pop(0)
            if self.isValid(cur, k):
                res = max(res, r - l + 1)
        return res

    def isValid(self, l: list, k: int) -> bool:
        count = defaultdict(int)
        s = 0
        m = 0
        for item in l:
            count[item] += 1
        for item in count:
            m = max(m, count[item])
        if len(l) - m <= k:
            return True
        else:
            return False



