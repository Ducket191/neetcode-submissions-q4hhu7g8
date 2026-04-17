class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        s, e = 0, len(points) - 1

        while s <= e:
            a, b = points[e]
            pivot = a * a + b * b
            left = s

            for i in range(s, e):
                x, y = points[i]
                if x * x + y * y < pivot:
                    points[left], points[i] = points[i], points[left]
                    left += 1

            points[left], points[e] = points[e], points[left]

            if left == k - 1:
                break
            elif left < k - 1:
                s = left + 1
            else:
                e = left - 1

        return points[:k]