"""
https://leetcode.com/problems/unique-binary-search-trees-ii/
Tree에서 재귀를 활용하면 풀 수 있음
재귀의 return, boundary를 어떻게 설정할 지 좀 고민하면 풀 수 있었
DP까지 사용하면 더 빠르게 얻을 수 있
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        arr = [i for i in range(1, n + 1)]
        dp = {}

        def recursive(nums):
            if len(nums) == 0:
                return []
            if len(nums) == 1:
                return [TreeNode(nums[0])]
            if nums in dp:
                return dp[nums]

            result = []
            for i in range(len(nums)):
                left = nums[:i]
                right = nums[i + 1:]
                if not left and right:
                    for r in recursive(right):
                        root = TreeNode(nums[i])
                        root.right = r
                        result.append(root)
                elif not right and left:
                    for l in recursive(left):
                        root = TreeNode(nums[i])
                        root.left = l
                        result.append(root)
                else:
                    for l in recursive(left):
                        for r in recursive(right):
                            root = TreeNode(nums[i])
                            root.left = l
                            root.right = r
                            result.append(root)
            dp[nums] = result
            return dp[nums]

        return recursive(tuple(arr))


