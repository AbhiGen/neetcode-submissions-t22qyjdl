class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        while left<right:
                midspeed=left+(right-left)//2
                totalhrs=0
                for pile in piles:
                        totalhrs+=math.ceil(pile/midspeed)
                if totalhrs<=h:
                        right=midspeed
                else:
                        left=midspeed+1
        return right