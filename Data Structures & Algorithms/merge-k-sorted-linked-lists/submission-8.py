import heapq
class Solution:    
    def mergeKLists(self, lists):
        heap = []
        counter = 0
        dummy = ListNode()
        curr = dummy
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, counter, node))
                counter += 1
        while heap:

            val, counter, node = heapq.heappop(heap)

   
            curr.next = node
            curr = curr.next


            if node.next:
                heapq.heappush(heap, (node.next.val, counter, node.next))
                counter += 1
        return dummy.next
    
        
