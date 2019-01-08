class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 0:
            return 0
        minPrice = prices[0]
        maxP = 0
        for price in prices:
            diff = price-minPrice
            if diff > maxP:
                maxP = diff
            if price < minPrice:
                minPrice = price
        return maxP
        