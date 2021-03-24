"""
https://leetcode.com/problems/word-search-ii/
DFS를 사용하고 Hash Table을 통해서 순회하는 과정에 일치하는 값이 있다면 결과 리스트에 넣었음
Trie를 사용해서도 구현할 수 있을 듯
"""
import collections
class Solution:
    def findWords(self, board, words) :
        table = collections.defaultdict(int)
        for word in words:
            table[word] = 1
        words.sort(reverse=True)
        result = []
        visited = [[False for _ in board[0]] for _ in board]

        def dfs(pos, idx, target):
            value = target[:idx + 1]
            if idx == len(target) - 1:
                if target not in result:
                    result.append(target)
                return
            if table[value] == 1 and value not in result:
                result.append(value)

            for i, j in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                n_col = pos[0] + i
                n_row = pos[1] + j
                if 0 <= n_col < len(board) and \
                        0 <= n_row < len(board[0]) and \
                        not visited[n_col][n_row] and \
                        board[n_col][n_row] == target[idx + 1]:
                    visited[n_col][n_row] = True
                    dfs((n_col, n_row), idx + 1, target)
                    visited[n_col][n_row] = False

        for col in range(len(board)):
            for row in range(len(board[0])):
                for word in words:
                    if board[col][row] == word[0] and word not in result:
                        visited[col][row] = True
                        dfs((col, row), 0, word)
                        visited[col][row] = False
        return result