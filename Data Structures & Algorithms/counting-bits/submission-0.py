class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        
        def helper(num):
            res=0
            while num>0:
                num=num&(num-1)
                res+=1
            return res
        
        for i in range(n+1):
            ans.append(helper(i))
        return ans

        