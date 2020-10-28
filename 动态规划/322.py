# Coin Change
"""
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1

Input: coins = [1], amount = 0
Output: 0
"""

def coinChange(coins, amount):
    
    # initialize dp[]
    dp = [0] + [float('inf')] * amount

    for coin in coins:
        for i in range(coin, amount+1):
            dp[i] = min(dp[i], dp[i-coin] + 1)
    
    return dp[-1] if dp[-1] != float('inf') else -1

print(coinChange([1,2,5],11))