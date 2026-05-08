class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        L = 0
        s = 0
        for R in range (len(arr)):
            s += arr[R]
            if R - L + 1 > k:
                s -= arr[L]
                L += 1
            if s / k >= threshold and R - L + 1 == k:
                res += 1

        return res 
            
        