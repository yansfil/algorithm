"""
https://leetcode.com/problems/sort-list/

LinkedList 버전의 mergeSort임
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeList(self, l1: ListNode, l2: ListNode):
        if not (l1 and l2):
            return l1 or l2

        head = merged = ListNode()

        while l1 and l2:
            if l1.val < l2.val:
                merged.next = l1
                l1 = l1.next
            else:
                merged.next = l2
                l2 = l2.next
            merged = merged.next
        merged.next = l1 or l2
        return head.next

    def sortList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        start = slow.next
        slow.next = None
        l, r = self.sortList(head), self.sortList(start)
        return self.mergeList(l, r)

