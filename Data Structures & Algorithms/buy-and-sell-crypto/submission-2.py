class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # L , R = 0 , len(prices) - 1
        minP = prices[0]
        maxP = 0
        for p in prices:
            minP = min(minP, p)
            maxP = max(p - minP, maxP)    
        return maxP    