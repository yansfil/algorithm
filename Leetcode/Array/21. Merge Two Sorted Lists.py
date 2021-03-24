"""
https://leetcode.com/problems/merge-two-sorted-lists/
Loop 안에서 양쪽의 크기를 비교하여 크기가 작은 Node를 한칸씩 옮긴다. 그리고 길이가 남은 링크드리스트는 바로 뒤에다 붙인다.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        left = l1
        right = l2
        root = cur = ListNode()
        while left and right:
            if right.val >= left.val:
                cur.next = ListNode(left.val)
                left = left.next
            else:
                cur.next = ListNode(right.val)
                right = right.next
            cur = cur.next
        if left:
            cur.next = left
        else:
            cur.next = right

        return root.next