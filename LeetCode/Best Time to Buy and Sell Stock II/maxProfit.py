class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if prices == None:
            return 0

        if len(prices) < 2:
            return 0

        profit = 0
        for i in range(len(prices[1:])):
            if prices[i + 1] > prices[i]:
                profit = profit + prices[i + 1] - prices[i]
        return profit

s=Solution()

input_data = [7,1,5,3,6,4] #maxProfit
print(s.maxProfit(input_data))