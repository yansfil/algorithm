"""
https://leetcode.com/problems/remove-invalid-parentheses/
Minimum Remove를 구한 후 BackTracking을 통해 valid parentheses를 구한다.
이때 visit 매개변수를 backtracking에 둬서 중복 접근을 방지해야 TLE에 거리지 않는다.
"""

import collections
class Solution:
    def removeInvalidParentheses(self, s: str) -> [str]:
        stack = []
        for char in s:
            if char == ")":
                if "(" in stack:
                    while stack and stack.pop() != "(":
                        pass
                else:
                    stack.append(char)
            else:
                stack.append(char)

        # 최소 (, ) Count하기
        _dict = collections.defaultdict(int)
        for k in stack:
            if k == ")":
                _dict[k] += 1
            if k == "(":
                _dict[k] += 1

        # 유효한지 확인하기
        def checkValid(s):
            stack = []
            for char in s:
                if char == ")":
                    if "(" in stack:
                        while stack and stack.pop() != "(":
                            pass
                    else:
                        return False
                else:
                    stack.append(char)
            return False if stack.count("(") or stack.count(")") else True

        result = set()
        visit = set()

        def dfs(s, op, cp, visit):
            if op == 0 and cp == 0:
                if checkValid(s):
                    result.add(s)
                return
            for idx in range(len(s)):
                if s[idx] == "(" and op > 0:
                    r = s[:idx] + s[idx + 1:]
                    if r not in visit:
                        visit.add(r)
                        dfs(r, op - 1, cp, visit)
                elif s[idx] == ")" and cp > 0:
                    r = s[:idx] + s[idx + 1:]
                    if r not in visit:
                        visit.add(r)
                        dfs(r, op, cp - 1, visit)

        dfs(s, _dict["("], _dict[")"], visit)
        return result