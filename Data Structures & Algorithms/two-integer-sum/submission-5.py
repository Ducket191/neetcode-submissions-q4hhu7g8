class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []  
        new_list = [target - x for x in nums]
        for i in range(len(nums)):
            new_new_list =  new_list[:i] + new_list[i+1:]
            if nums[i] in new_new_list:
                output.append(i)
        return output