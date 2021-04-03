"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Traverse(Recursive)하게 풀 때, 전역 변수를 적극적으로 활용할 수 있는지 생각하기
1번 : In-Order로 조회하면서 전역변수로 값을 찾음
2번 : Binary Tree의 특성을 이용해 left의 count를 재고 이를 통해 Recursive하게 파고 가기
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # 전역 변수로 문제 풀기
        self.result = 0
        self.k = k
        def dfs(node):
            if not node : return
            dfs(node.left)
            self.k -= 1
            if self.k == 0:
                self.result = node.val
                return
            dfs(node.right)
        dfs(root)
        return self.result

        # count로 풀기
        def count(node):
            if not node: return 0
            return count(node.left) + count(node.right) + 1

        def dfs(node, kk):
            cnt = count(node.left)
            if cnt + 1 == kk:
                return node.val
            elif kk <= cnt:
                return dfs(node.left, kk)
            else:
                return dfs(node.right, kk - cnt - 1)

        return dfs(root, k)


