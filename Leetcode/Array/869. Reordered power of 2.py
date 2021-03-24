"""
https://leetcode.com/problems/reordered-power-of-2/
모든 경우의 수를 다 대입하는 방식보다 역으로 답으로 부터 값을 찾으면 빠르게 문제 해결할 수도 있다.
"""

import collections

class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        s = sorted(str(N))
        i = 1
        while i < N * 10:
            if s == sorted(str(N)):
                return 1
            i *= 2
        return 0