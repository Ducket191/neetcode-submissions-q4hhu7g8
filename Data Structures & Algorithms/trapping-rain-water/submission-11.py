class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        prefix = []
        surfix = []
        maxp, maxs = 0, 0
        res = 0
        for item in height:
            prefix.append(maxp)
            maxp = max(maxp, item)

        for i in range(len(height)-1, -1, -1):
            surfix.append(maxs)
            maxs = max(maxs, height[i])
        surfix.reverse()

        for i in range(len(height)):
            w = min(prefix[i], surfix[i]) - height[i]
            if w > 0:
                res += w
        return res
