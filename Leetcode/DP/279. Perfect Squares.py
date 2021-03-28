"""
https://leetcode.com/problems/perfect-squares/
DP 문제
"""

import math
class Solution:
    def numSquares(self, n: int) -> int:
        if n == (int(n**0.5))**2:
            return 1
        dp = [n] * (n+1)
        dp[0] =1
        for i in range(1,n+1):
            if i**.5%1 == 0 :
                dp[i] = 1
            else :
                for j in range(1,math.floor(i**.5)+1) :
                    dp[i] = min(dp[i], dp[i-j**2]+1)
        return dp[n]