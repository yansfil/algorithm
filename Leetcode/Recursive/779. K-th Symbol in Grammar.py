"""
https://leetcode.com/problems/k-th-symbol-in-grammar/
1 -> 규칙을 찾는다 (재귀로 해결될 것 같은 느낌이 들면 얼렁 규칙을 찾아보자)
2 -> 재귀를 적용한다
"""

class Solution:
    def kthGrammar(self, N: int, K: int) -> int:

        def recursive(K, cnt=0):
            if K == 1:
                return cnt
            i = 1
            while i < K:
                i *= 2
            return recursive(K - (i // 2), cnt + 1)

        cnt = recursive(K, 0)
        return 0 if cnt % 2 == 0 else 1
