from math import ceil


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        if not head.next:
            return head
        cur = head.next
        end = cur.val
        length = 1
        while cur.next:
            length += 1
            cur = cur.next
            if cur.val > end:
                end = cur.val
        result = head
        for i in range(0, ceil(length / 2)):
            result = result.next

        return result
