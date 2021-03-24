"""
https://leetcode.com/problems/01-matrix/submissions/
보통 최소 길이를 구해야하는 상황에서는 BFS를 쓰는게 맞다.
최대 길이의 경우 BFS,DFS 모두 가능하겟지만,
"""


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:

        m = len(matrix)
        n = len(matrix[0])
        for c in range(m):
            for r in range(n):
                if matrix[c][r] == 1:
                    queue = [[(c, r), 1]]
                    while queue:
                        original_point, distance = queue.pop(0)
                        o_col, o_row = original_point
                        for col, row in [(o_col + 1, o_row), (o_col - 1, o_row), (o_col, o_row + 1),
                                         (o_col, o_row - 1)]:
                            if 0 <= col < m and 0 <= row < n:
                                if matrix[col][row] == 0:
                                    matrix[c][r] = distance
                                    queue = []
                                    break
                                else:
                                    queue.append([(col, row), distance + 1])

        return matrix
