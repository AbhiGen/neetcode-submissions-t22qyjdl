class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left=max(weights)
        right=sum(weights)

        while left<right:
            midweight=left+(right-left)//2
            daysneeded=1
            currweight=0
            for weight in weights:
                if currweight+weight>midweight:
                    daysneeded+=1
                    currweight=0
                currweight+=weight
            if daysneeded<=days:
                right=midweight
            else:
                left=midweight+1
        return left