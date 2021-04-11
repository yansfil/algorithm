"""
https://leetcode.com/problems/ones-and-zeroes/
풀이 : https://leetcode.com/problems/ones-and-zeroes/discuss/177368/Python-Clear-Explanation-from-Recursion-to-DP

1. BackTracking으로 먼저 문제를 접근하기
2. 만약 TLE에 걸릴 것 같다면?
3. Optimal SubProblem이 가능한지 & 순차적인 접근으로 Memoization이 가능한지 확인하기
4. TOP DOWN & Bottom UP 어떻게 할지 생각하기

[느낀 점]
순회를 할 때 꼭 For Loop & Visited로만 생각하지 말기 - Graph 문제가 아닌 이상 다른 접근 방법이 있을 수 있다

"""
import collections

#기존에 풀었던 방식 -> TLE
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # BackTracking
        memo = {}
        visited = set()

        def findMax(m, n, visited):
            counter = 0
            for idx in range(len(strs)):
                if (strs[idx], idx) not in visited:
                    c = collections.Counter(strs[idx])
                    visited.add((strs[idx], idx))
                    if m - c["0"] >= 0 and n - c["1"] >= 0:
                        counter = max(counter, findMax(m - c["0"], n - c["1"], visited) + 1)
                    visited.remove((strs[idx], idx))
            return counter

        return findMax(m, n, visited)

#Top-Down 방식
"""
순회하는 위치를 매개변수로 처리하고 있다&없다로 경우의 수를 좁혀 Memoization이 가능한 로직
"""

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # BackTracking
        memo = {}

        def findMax(strs, i, m, n):
            if (i, m, n) in memo:
                return memo[(i, m, n)]
            counter = 0
            if i <= len(strs) - 1:
                if m > 0 or n > 0:
                    v1 = findMax(strs, i + 1, m, n)

                    c = collections.Counter(strs[i])
                    _m = m - c["0"]
                    _n = n - c["1"]
                    v2 = 0
                    if _m >= 0 and _n >= 0:
                        v2 = findMax(strs, i + 1, _m, _n) + 1
                    counter = max(v1, v2)
                    memo[(i, m, n)] = counter
            return counter

        return findMax(strs, 0, m, n)

#Bottom-Up (KnapSack 방식)
class Solution:
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        length = len(strs)
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]

        for s in strs:
            m1, n1 = 0, 0
            for ch in s:
                if ch == '0':
                    m1 += 1
                else:
                    n1 += 1

            for j in range(m, m1 - 1, -1):
                for k in range(n, n1 - 1, -1):
                    # can be used, so choose to use or skip
                    if j >= m1 and k >= n1:
                        dp[j][k] = max(dp[j][k], dp[j - m1][k - n1] + 1)

        return dp[-1][-1]