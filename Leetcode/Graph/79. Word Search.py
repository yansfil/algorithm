"""
https://leetcode.com/problems/word-search/
DFS를 사용했으며 방문여부를 확인할 list를 사용했다.
코드를 조금 더 깔끔하게 하려면 any를 사용해서 루프 안에서 재귀로 사용되는 구문을 처리할 수 있음
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        def dfs(point, left, visited):
            if not left:
                return True
            for col, row in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                col_n = point[0] + col
                row_n = point[1] + row
                if 0 <= col_n <= m - 1 and 0 <= row_n <= n - 1 and not visited[col_n][row_n]:
                    if board[col_n][row_n] == left[0]:
                        visited[col_n][row_n] = True
                        if dfs((col_n, row_n), left[1:], visited):
                            return True
                        visited[col_n][row_n] = False
            return False

        for col in range(m):
            for row in range(n):
                if board[col][row] == word[0]:
                    visited[col][row] = True
                    if dfs((col, row), word[1:], visited):
                        return True
                    visited[col][row] = False
        return False
