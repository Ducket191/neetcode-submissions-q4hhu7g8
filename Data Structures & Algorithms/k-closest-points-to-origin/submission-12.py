class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = self.quickSort(points, k, 0, len(points)-1)
        return res[:k]
    def quickSort(self, points: List[List[int]], k: int, s: int, e: int) -> List[List[int]]:
        if e - s + 1 <= 1:
            return points
        a,b = points[e]
        pivot = a**2 + b**2
        left = s
        for i in range(s, len(points)):
            x,y = points[i]
            if x**2 + y**2 < pivot:
                tmp = points[left]
                points[left] = points[i]
                points[i] = tmp
                left += 1
        tmp = points[left]
        points[left] = points[e]
        points[e] = tmp
        if left == k-1:
            return points[:k]
        elif left < k-1:
            self.quickSort(points, k, left+1, e)
        elif left > k:
            self.quickSort(points, k, s, left-1)
        return points
            