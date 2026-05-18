class Solution {
    public int maxProfit(int[] prices) {
        int mincost=prices[0];
        int maxprofit=0;
        for(int i=1;i<prices.length;i++){
            if(prices[i]<mincost){
                mincost=prices[i];
            }
            maxprofit=Math.max(prices[i]-mincost,maxprofit);
        }
        return maxprofit;
    }
}
