class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in range(len(nums)):
            count[nums[i]]=count.get(nums[i],0)+1
        freq=[[] for i in range(len(nums)+1)]
        for item in count:
            freq[count[item]].append(item)
        res=[]
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                res.append(j)
                if len(res)==k:
                    return res
                
                    
