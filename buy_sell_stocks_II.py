class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total = 0

        for i in range(len(prices)-1):
          if prices[i+1] > prices[i]:
            total += prices[i+1] - prices[i]
        return total


obj = Solution()
obj.maxProfit([7,1,5,3,6,4])