"""
https://leetcode.com/problems/brace-expansion-ii/
참고 : https://leetcode.com/problems/brace-expansion-ii/discuss/409894/Python-with-explanation-Stack-solution.
{ , } 문자 이렇게 4가지 케이스에 맞게 대응한다
곱과 합을 처리하기 위해 { 와 , 에서는 여유 버퍼로 [""] 를 넣어준다.
"""


# Input: "{a,b}{c,{d,e}}"
# Output: ["ac","ad","ae","bc","bd","be"]

def braceExpansionII(self, expression):
    stack = [[""]]
    if not expression:
        return []
    for v in expression:
        if v == "{":
            stack.append(v)
            stack.append([""])
        elif v == ",":
            stack.append([""])
        elif v == "}":
            union = []
            while stack and stack[-1] != "{":
                union += stack.pop()
            stack.pop()

            stack[-1] = [vo + u for vo in stack[-1] for u in union]
        else:
            stack[-1] = [c + v for c in stack[-1]]
    res = set()
    while stack:
        ele = stack.pop()
        for x in ele:
            res.add(x)
    return sorted(res)