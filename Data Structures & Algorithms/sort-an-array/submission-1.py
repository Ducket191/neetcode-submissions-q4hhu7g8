class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(arr, s, e):
            if e - s + 1 <= 1:
                return arr
            
            m = (e+s) // 2
            mergeSort(arr, s, m)
            mergeSort(arr, m+1, e)

            merge(arr, s, m, e)

            return arr
        def merge(arr, s, m, e):
            L = arr[s:m+1]
            R = arr[m+1:e+1]
            x, y = 0, 0
            for i in range(s, e + 1):
                if x < len(L) and y < len(R):
                    if L[x] <= R[y]:
                        arr[i] = L[x]
                        x += 1
                    else:
                        arr[i] = R[y]
                        y += 1
                elif x >= len(L):
                    arr[i] = R[y]
                    y += 1
                elif y >= len(R):
                    arr[i] = L[x]
                    x += 1
            return arr
        return mergeSort(nums, 0, len(nums)-1)
