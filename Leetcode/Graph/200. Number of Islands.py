"""
https://leetcode.com/problems/number-of-islands/submissions/
DFS와 BFS로 모두 접근할 수 있는 문제이다. 방문 여부를 visited listed 변수로 관리해주면 쉽게 풀린다.
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid[0])
        n = len(grid)
        visited = [[0 for _ in range(m)] for _ in range(n)]

        ### BFS ###
        count = 0
        for i in range(m):
            for j in range(n):
                if not visited[j][i] and grid[j][i] == "1":
                    count += 1
                    queue = [(j, i)]
                    while queue:
                        col, row = queue.pop()
                        for x, y in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                            col_new = col + y
                            row_new = row + x
                            if 0 <= col_new <= n - 1 and 0 <= row_new <= m - 1 and not visited[col_new][row_new] and \
                                    grid[col_new][row_new] == "1":
                                visited[col_new][row_new] = 1
                                queue.append((col_new, row_new))

                                ### DFS ###
        # def dfs(col,row):
        #     for x,y in [[1,0],[0,1],[-1,0],[0,-1]]:
        #         col_new = col+y
        #         row_new = row+x
        #         if 0 <= col_new <= n-1 and 0 <= row_new <= m-1 and not visited[col_new][row_new] and grid[col_new][row_new] == "1":
        #             visited[col_new][row_new] = 1
        #             dfs(col_new,row_new)
        # for i in range(m):
        #     for j in range(n):
        #         if not visited[j][i] and grid[j][i] == "1":
        #             dfs(j,i)
        #             count += 1
        return count