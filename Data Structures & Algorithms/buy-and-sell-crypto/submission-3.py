class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        minprice=float('inf')
        for i in range(len(prices)):
            if prices[i]<minprice:
                minprice=prices[i]
            maxprofit=max(maxprofit,prices[i]-minprice)
        return maxprofit
        