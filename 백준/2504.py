"""
https://www.youtube.com/watch?v=II3rISJtNS0
"""

def get_value(string):
    table = {
        "(" : ")",
        "[" : "]"
    }
    stack = []
    result = 1
    for char in string:
        if char in table:
            stack.append(char)
        elif stack and char == table[stack[-1]]:
            stack.pop()

        else :
            return 0


    #올바르지 못하면 0
    #