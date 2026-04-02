class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            x = -1
            for j in range(i+1, len(arr)):
                if arr[j] > x:
                    x = arr[j]
            arr[i] = x
        return arr