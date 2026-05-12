class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        for r in range(1, len(height)):
            if height[r] > height[r-1]:
                if stack:
                    lastlv = height[r-1]
                    while stack and stack[-1][0] < height[r]:
                        curh, curids = stack.pop()
                        lv = curh - lastlv
                        res += (r - curids-1)*lv
                        lastlv = curh
                    if stack:
                        lv = height[r] - lastlv
                        res += (r - stack[-1][1]-1)*lv
            elif height[r] < height[r-1]:
                stack.append([height[r-1], r-1])
        return res
        