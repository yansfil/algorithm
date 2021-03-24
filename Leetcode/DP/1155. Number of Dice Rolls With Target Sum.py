"""
https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
DP를 이용해서 푸는 문제
DP를 사용해야겠다는 건 알고 있었으나 어떤 식으로 공식을 써야할지 감이 잘 안왔다.
이차원 DP 풀어보는 걸 더 연습하자.
"""

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0] * (target+1) for _ in range(d+1)]
        dp[0][0] = 1
        for i in range(1,d+1):
            for j in range(1,target+1):
                dp[i][j] = sum([dp[i-1][j-k] for k in range(1,f+1) if j-k >= 0 ])
        return dp[-1][-1] % (10**9 + 7)