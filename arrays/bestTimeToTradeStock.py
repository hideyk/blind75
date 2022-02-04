from typing import List

def maxProfit(prices: List[int]) -> int:
    profit = 0
    if len(prices) < 2: return 0
    
    l, r = 0, 1
    for i in range(len(prices)):
        if prices[i] < prices[l]:
            l, r = i, i + 1
            continue
        elif prices[i] > prices[l] and prices[i] > prices[r]:
            r = i
        
        profit = max(profit, prices[r]-prices[l])
        
    return profit