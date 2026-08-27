class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[-1]*len(nums1)
        nums1index={}
        for i in range(len(nums1)):
            nums1index[nums1[i]]=i
        stack=[]
        for i in range(len(nums2)):
            curr=nums2[i]
            while stack and curr>stack[-1]:
                val=stack.pop()
                idx=nums1index[val]
                res[idx]=curr
            if curr in nums1index:
                stack.append(curr)
        return res

        