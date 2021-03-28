"""
https://leetcode.com/problems/all-possible-full-binary-trees/
기본적인 BackTracking 유형과 Memoization을 정리해야할 것 같다.

시간복잡도:
공간복잡도:
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.memo = {}
        self.memo[0] = []
        self.memo[1] = [TreeNode(0)]

    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        ans = []
        if n in self.memo:
            return self.memo[n]

        for i in range(1, n, 2):
            lefts = self.allPossibleFBT(i)
            rights = self.allPossibleFBT(n - i - 1)

            for left in lefts:
                for right in rights:
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    ans.append(root)
        self.memo[n] = ans
        return ans