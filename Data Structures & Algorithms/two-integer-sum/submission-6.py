class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps={}
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in maps:
                return [maps[complement],i]
            else:
                maps[nums[i]]=i
        return -1
        