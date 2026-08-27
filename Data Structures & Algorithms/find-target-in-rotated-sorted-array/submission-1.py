class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left<right:
            mid=left+(right-left)//2
            if nums[mid]>nums[right]:
                left=mid+1
            else:
                right=mid
        pivot=left
        def binarys(left,right):
            while left<=right:
                mid=left+(right-left)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]>target:
                    right=mid-1
                else:
                    left=mid+1
            return -1
        if target>=nums[pivot] and target<=nums[len(nums)-1]:
            return binarys(pivot,len(nums)-1)
        else:
            return binarys(0,pivot-1)
        