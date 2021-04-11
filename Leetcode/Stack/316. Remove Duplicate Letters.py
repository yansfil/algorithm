"""
https://leetcode.com/problems/remove-duplicate-letters/

그리디하게 풀 수 있는 문제
counter가
"""

import collections
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = collections.Counter(s)
        result = []
        stack = [s[0]]
        for i in range(1, len(s)):
            if counter[s[i]] == 1:
                result.append(s[i])
            else:
                if stack[-1] < s[i]:
                    stack.append(s[i])
                else:
                    while stack and stack[-1] > s[i]:
                        v = stack.pop()
                        if counter[v] > 1:
                            counter[v] -= 1
                        else:
                            result.append(v)
                    stack.append(s[i])
        return "".join(result + stack)
