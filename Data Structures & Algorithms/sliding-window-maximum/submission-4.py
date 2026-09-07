import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        r=k
        heap = []
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        res = [-heap[0][0]]
        while r < len(nums):
            l += 1
            heapq.heappush(heap, (-nums[r], r))
            while heap[0][1] < l:
                heapq.heappop(heap)
            res.append(-heap[0][0])
            r += 1
        return res

            