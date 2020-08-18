class Solution(object):
    def maxProfit(self, prices):
        
        n=len(prices)
        if n<=1:
            return 0
        maxprofit=0
        low=prices[0]
        for i in range(1,n):
            low=min(low,prices[i])
            maxprofit=max(maxprofit, prices[i]-low)
        return maxprofit