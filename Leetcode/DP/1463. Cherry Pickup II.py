"""
https://leetcode.com/problems/cherry-pickup-ii/
DP를 정확히 사용할 수 있는가
Recursive를 잘 활용할 수 있는가
"""
class Solution:
    def __init__(self):
        self.dp = []

    def cherryPickup(self, grid: List[List[int]]) -> int:
        self.dp = {}

        def dfs(pos_a, pos_b, level=0):
            if level == len(grid):
                return 0
            if (level, pos_a, pos_b) in self.dp:
                return self.dp[(level, pos_a, pos_b)]
            result = grid[level][pos_a] + grid[level][pos_b]
            if pos_a == pos_b:
                result = result // 2
            max_v = -float('inf')
            for a_row in [-1, 0, 1]:
                for b_row in [-1, 0, 1]:
                    a, b = pos_a + a_row, pos_b + b_row
                    if 0 <= a < len(grid[0]) and 0 <= b < len(grid[0]):
                        max_v = max(max_v, dfs(a, b, level + 1))
            self.dp[(level, pos_a, pos_b)] = result + max_v
            return self.dp[(level, pos_a, pos_b)]

        result = dfs(0, len(grid[0]) - 1, 0)
        print(self.dp)
        return result