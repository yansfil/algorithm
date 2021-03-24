"""
https://leetcode.com/problems/surrounded-regions/
정방향과 역방향으로 문제를 풀 수 있다.
항상 문제를 풀 때 경우의 수를 좁히고 단순하게 풀 수 있는 방법이 있나 생각해본다
이때 경계조건(정답과 직결되는 부분)부터 역으로 접근하는 접근법은 경우의 수, 난이도를 크게 좁힐 수 있다.
"""


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        visited = [[0] * n for _ in range(m)]

        def recursive(col, row):
            if board[col][row] == "O":
                visited[col][row] = 1
                for c, r in [(col + 1, row), (col - 1, row), (col, row - 1), (col, row + 1)]:
                    if 0 <= c < m and 0 <= r < n and board[c][r] == "O" and visited[c][r] == 0:
                        recursive(c, r)

        for row in range(n):
            recursive(0, row)
            recursive(m - 1, row)

        for col in range(m):
            recursive(col, 0)
            recursive(col, n - 1)

        for col in range(m):
            for row in range(n):
                if board[col][row] == "O":
                    if visited[col][row] == 0:
                        board[col][row] = "X"
