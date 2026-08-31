"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash = {}

        # Create copies
        temp = head
        while temp:
            hash[temp] = Node(temp.val)
            temp = temp.next

        # Connect copies
        temp = head
        while temp:
            hash[temp].next = hash[temp.next] if temp.next else None
            hash[temp].random = hash[temp.random] if temp.random else None
            temp = temp.next

        return hash[head] if head else None
