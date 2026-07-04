class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b=prices[0]
        p=0
        if len(prices)==1:
            return 0
        for i in range(1,len(prices)):
            if prices[i]<b:
                b=prices[i]

            c=prices[i]-b
            if c>p:
                p=c
        return p

        return p