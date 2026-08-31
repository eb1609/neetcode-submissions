class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        width = 0
        for i, height in enumerate(heights):
            while stack and height < heights[stack[-1]]:
                index = stack.pop()
                h = heights[index]
                if stack:
                    width = i-stack[-1]-1
                else:
                    width = i
                maxArea = max(maxArea, h * width)

            stack.append(i)
        while stack:
            index = stack.pop()
            h = heights[index]

            if stack:
                width = len(heights) - stack[-1] - 1
            else:
                width = len(heights)

            maxArea = max(maxArea, h * width)

        return maxArea