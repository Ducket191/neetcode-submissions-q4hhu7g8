class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        # Instead of lv, we track the height of the floor we just processed
        for r in range(1, len(height)):
            if height[r] > height[r-1]:
                # last_height starts as the height of the bar immediately to the left
                last_height = height[r-1] 
                
                while stack and stack[-1][0] < height[r]:
                    cur_h, cur_idx = stack.pop()
                    # Height of this water slice is (this bar's height - floor)
                    h_diff = cur_h - last_height
                    res += (r - cur_idx - 1) * h_diff
                    last_height = cur_h # Update floor to the height of the bar we just processed
                
                if stack:
                    # If there's still a bar in the stack, it's >= height[r]
                    # The water level for this final slice is capped at height[r]
                    h_diff = height[r] - last_height
                    res += (r - stack[-1][1] - 1) * h_diff
            
            elif height[r] < height[r-1]:
                # Only push to stack when height decreases, creating a potential left wall
                stack.append([height[r-1], r-1])
                
        return res