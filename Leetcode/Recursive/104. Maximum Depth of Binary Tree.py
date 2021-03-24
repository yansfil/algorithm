"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/
간단하게 재귀로 풀 수 있는 문제임
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        def dfs(node):
            if not node:
                return 0
            return max(dfs(node.right),dfs(node.left))+1
        return dfs(root)