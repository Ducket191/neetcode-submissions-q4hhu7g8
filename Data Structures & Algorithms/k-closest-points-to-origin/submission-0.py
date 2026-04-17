import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Sort the points based on their distance from origin
        # We don't even need sqrt() because x^2 + y^2 maintains the same order
        points.sort(key=lambda p: p[0]**2 + p[1]**2)
        
        # Return the first k points
        return points[:k]