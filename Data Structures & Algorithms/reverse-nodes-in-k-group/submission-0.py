# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        for _ in range(k):
            if not temp:
                return head
            temp = temp.next
        prev = None
        h = head

        for _ in range(k):
            next_node = h.next
            h.next = prev
            prev = h
            h = next_node
        head.next = self.reverseKGroup(h, k)
        return prev