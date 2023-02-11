class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        l = 0
        maxProfit = 0

        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            maxProfit = max(maxProfit, prices[r] - prices[l])

        return maxProfit