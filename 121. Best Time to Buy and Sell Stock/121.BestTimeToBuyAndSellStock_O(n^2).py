class Solution(object):
    def maxProfit(self, prices):

        max_i = 0
        max_j = 0
        max_profit = 0
        for i in range(len(prices) - 1):
            for j in range(i+1, len(prices)):
                if prices[j] - prices[i] > max_profit:
                    max_profit = prices[j] - prices[i]
        return max_profit