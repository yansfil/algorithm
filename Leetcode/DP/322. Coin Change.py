"""
https://leetcode.com/problems/coin-change/
대표적인 DP 문제로 그리디로 풀 수 없는 문제임.
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            min_v = float('inf')
            for coin in coins:
                if i - coin >= 0  :
                    min_v = min(min_v, dp[i-coin]+1)
            dp[i] = min_v
        return -1 if dp[-1] == float('inf')else dp[-1]