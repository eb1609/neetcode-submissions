class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ptr1 = 0
        ptr2 = len(heights)-1
        maxVal = 0
        while ptr1<ptr2:
            minVal = min(heights[ptr1],heights[ptr2])
            maxVal = max(maxVal,minVal*(ptr2-ptr1))
            if minVal == heights[ptr1]:
                ptr1+=1
            else:
                ptr2-=1
        return maxVal