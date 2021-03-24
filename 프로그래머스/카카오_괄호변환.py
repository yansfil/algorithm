def solution(p):
    answer = ''

    def _split(p):
        open = 0
        close = 0
        for i in range(len(p)):
            if p[i] == "(":
                open += 1
            else:
                close += 1
            if open == close:
                return [p[:i + 1], p[i + 1:]]
        return ["",""]
    def _check(word):
        stack = []
        for w in word:
            if w == "(":
                stack.append(w)
            else:
                if stack:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

    def recursive(word):
        u, v = _split(word)
        if not u:
            return ""
        if _check(u):
            return u + recursive(v)
        else:
            string = "(" + recursive(v) + ")"
            for i in u[1:-1]:
                if i == "(":
                    string += ")"
                else:
                    string += "("
            return string

    return recursive(p)
print(solution(")())(("))