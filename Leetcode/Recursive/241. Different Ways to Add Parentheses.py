"""
https://leetcode.com/problems/different-ways-to-add-parentheses/

Operator를 기준으로 쪼개고 List끼리 서로 연산시켜 경우의 수를 구하는 문제

"""


class Solution:
    def compute(self, x, y, op):
        result = []
        for a in x:
            for b in y:
                result.append(eval(str(a) + op + str(b)))
        return result

    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isdigit():
            return [input]
        result = []
        for idx, v in enumerate(input):
            if v in "*-+":
                a = self.diffWaysToCompute(input[:idx])
                b = self.diffWaysToCompute(input[idx + 1:])
                result.extend(self.compute(a, b, v))
        return result