class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        h = min(heights[l],heights[r])
        a = r-l
        res = h*a
        curl = heights[l]
        curr = heights[r]
        while l < r:
            if heights[l] < heights[r]:
                l += 1
                curl = heights[l]
            elif heights[l] > heights[r]:
                r -= 1
                curr = heights[r]
            elif heights[r] == heights[l]:
                l += 1
            h,a = min(heights[l],heights[r]), r-l
            res = max(res, h*a)
        return res

