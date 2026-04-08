class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currmax=1
        currmin=1
        res=nums[0]
        for num in nums:
            temp=currmax*num
            currmax=max(num,num*currmax,num*currmin)
            currmin=min(num,temp,currmin*num)
            res=max(res,currmax)
        return res