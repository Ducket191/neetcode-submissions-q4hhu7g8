class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = j = 0
        c = 0
        n1 = nums1[:m]
        while i < m and j < n:
            if n1[i] <= nums2[j]:
                nums1[c] = n1[i]
                i += 1
                c += 1
            else:
                nums1[c] = nums2[j]
                j += 1
                c += 1

        while i < m:
            nums1[c] = n1[i]
            i += 1
            c += 1
        while j < n:
            nums1[c] = nums2[j]
            j += 1
            c += 1