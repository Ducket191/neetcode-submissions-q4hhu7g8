class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        pre = [0]
        for n in nums:
            total += n
            pre.append(total)
        total = 0
        sur = [0]
        for n in nums[::-1]:
            total += n
            sur.append(total)
        sur.reverse()
        for i in range(len(nums)):
            if pre[i] == sur[i+1]:
                return i
        return -1