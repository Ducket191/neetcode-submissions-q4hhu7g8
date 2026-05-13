class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax <= rightMax:
                l += 1
                if height[l] > leftMax:
                    leftMax = height[l]
                else:
                    res += leftMax - height[l]
            else:
                r -= 1
                if height[r] > rightMax:
                    rightMax = height[r]
                else:
                    res += rightMax - height[r]

        return res
                
