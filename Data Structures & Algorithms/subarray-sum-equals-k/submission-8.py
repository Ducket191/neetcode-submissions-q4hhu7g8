class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        total = 0
        prefix = [0]
        contain = defaultdict(int)
        for n in nums:
            total += n
            prefix.append(total)
            contain[total] += 1
        for i in range(len(nums)):
            target = k + prefix[i]
            if target in contain:
                res += contain[target]
            contain[prefix[i+1]] -= 1
        return res