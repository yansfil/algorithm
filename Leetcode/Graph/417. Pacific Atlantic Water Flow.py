"""
https://leetcode.com/problems/pacific-atlantic-water-flow/submissions/
DFS와 BFS로 모두 접근할 수 있는 문제이다. 순회하는 것을 꼭 정방향으로만 생각하지말고 역방향으로 생각해보자.
조건이 만족될 때까지 내려가기, 조건이 만족됐다고 가정하고 시작해보는 것이 효과적일 수 있다.
"""

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        m = len(matrix[0])
        n = len(matrix)
        pa, at = set(), set()
        ### DFS ###
        def dfs(col, row, explored, prev):
            if not (0 <= col <= n - 1) or not (0 <= row <= m - 1) or (col, row) in explored or matrix[col][row] < prev:
                return
            explored.add((col, row))
            for x, y in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                dfs(col + y, row + x, explored, matrix[col][row])

        for i in range(m):
            dfs(0, i, pa, matrix[0][i])
            dfs(n - 1, i, at, matrix[n - 1][i])
        for j in range(n):
            dfs(j, 0, pa, matrix[j][0])
            dfs(j, m - 1, at, matrix[j][m - 1])

        ### BFS ###
        def bfs(col,row,s):
            queue = [(col,row)]
            while queue:
                col,row = queue.pop()
                s.add((col,row))
                for x,y in [[0,1],[1,0],[-1,0],[0,-1]]:
                    if 0 <= col+y <= n-1 and 0 <= row+x <= m-1 and not (col+y,row+x) in s and matrix[col+y][row+x] >= matrix[col][row]:
                        queue.append((col+y, row+x))
        for i in range(m):
            bfs(0,i,pa)
            bfs(n-1,i,at)
        for j in range(n):
            bfs(j,0,pa)
            bfs(j,m-1,at)

        return list(pa & at)
