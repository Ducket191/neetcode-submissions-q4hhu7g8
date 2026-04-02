class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums.sort()
        s = sorted(set(nums))
        left = 0
        max_len = 0
        w = []
        for right in range (len(s)):
            w.append(s[right])
            if s[right] - s[left] == len(w) - 1:
                max_len = max(max_len, right - left + 1)
            else:
                while s[right] - s[left] != len(w) - 1:
                    w.remove(s[left])
                    left += 1
        return max_len