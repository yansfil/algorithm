"""
https://leetcode.com/problems/longest-valid-parentheses/

나는 별도의 Valid 배열을 사용했음
"""

#내가 푼 문제
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        valid_arr = [0] * len(s)
        stack = []
        for idx in range(len(s)):
            if s[idx] == "(":
                stack.append(("(", idx))
            else:
                if stack and stack[-1][0] == "(":
                    v, i = stack.pop()
                    valid_arr[i] = 1
                    valid_arr[idx] = 1
                else:
                    stack.append((")", idx))
        max_length = 0
        cnt = 0
        for i in range(len(valid_arr)):
            if valid_arr[i] == 1:
                cnt += 1
                if i == len(valid_arr) - 1:
                    max_length = max(cnt, max_length)
            elif valid_arr[i] == 0:
                max_length = max(cnt, max_length)
                cnt = 0
        return max_length

class Solution:
    def longestValidParentheses(self, s: str) -> int:

        # stack, used to record index of parenthesis
        # initialized to -1 as dummy head for valid parentheses length computation
        stack = [-1]

        max_length = 0

        # linear scan each index and character in input string s
        for cur_idx, char in enumerate(s):

            if char == '(':

                # push when current char is (
                stack.append(cur_idx)

            else:

                # pop when current char is )
                stack.pop()

                if not stack:

                    # stack is empty, push current index into stack
                    stack.append(cur_idx)
                else:
                    # stack is non-empty, update maximal valid parentheses length
                    max_length = max(max_length, cur_idx - stack[-1])

        return max_length