class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        m = 0
        c = arr[-1]
        for i in range(len(arr)-2, -1, -1):
            m = max(c, m)
            c = arr[i]
            arr[i] = m
        arr[-1] = -1
        return arr
