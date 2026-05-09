class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l = 0
        res = 0
        if len(arr) == 1:
            return 1
        if len(arr) == 2:
            if arr[0] == arr[1]:
                return 1
            else:
                return 2
        for r in range(1, len(arr)-1):
            if arr[r] == arr[r+1]:
                l = r + 1
            elif arr[r-1] == arr[r]:
                l = r
            else:
                if (arr[r-1] > arr[r]) == (arr[r] > arr[r+1]):
                    l = r
            res = max(res, r-l+1)
        return res + 1
        