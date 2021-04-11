"""
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Serialization & Deserialization
BFS 방식으로 Level 별로 내려가면서 노드를 추가하고, 이를 바탕으로 순차적으로 left,right에 값을 부여하면서 Deserialization했음
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import collections
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        queue = collections.deque([root])
        strings = ['#']
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
                strings.append(node.val)
            else:
                strings.append("#")
        return " ".join(map(str, strings))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        strings = data.split()
        if strings[1] == "#":
            return None
        root = TreeNode(strings[1])
        queue = collections.deque([root])
        index = 2
        while queue:
            node = queue.popleft()
            if strings[index] != "#":
                node.left = TreeNode(strings[index])
                queue.append(node.left)
            index += 1
            if strings[index] != "#":
                node.right = TreeNode(strings[index])
                queue.append(node.right)
            index += 1
        return root