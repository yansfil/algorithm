"""
https://leetcode.com/problems/spiral-matrix/
상하좌우 각기 다른 움직임을 가져가므로 반복적으로 상하좌우를 가져가면서 result에 값들을 넣는다.
나는 matrix input값을 mutate했지만, 다른 상태 변수로 작업하는 게 더 깔끔해 보임
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        length = len(matrix) * len(matrix[0])
        result = []
        while matrix:
            for i in [1, 2, 3, 4]:
                if i == 1 and matrix:
                    result += matrix.pop(0)
                if i == 2 and matrix and len(matrix[0]):
                    for rows in matrix:
                        result.append(rows.pop())
                if i == 3 and matrix:
                    result += matrix.pop()[::-1]
                if i == 4 and matrix and len(matrix[0]):
                    for i in range(len(matrix) - 1, -1, -1):
                        result.append(matrix[i].pop(0))
        return result

