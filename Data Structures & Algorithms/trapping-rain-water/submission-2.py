class Solution:
    def trap(self, height: List[int]) -> int:
        ptr1 = 0
        ptr2 = len(height)-1
        leftMax = 0
        rightMax = 0
        water = 0
        while ptr1<ptr2:
            if height[ptr1]<height[ptr2]:
                if height[ptr1] >= leftMax:
                    leftMax = height[ptr1]
                else:
                    water += leftMax - height[ptr1]

                ptr1 += 1
            else:
                if height[ptr2]>=rightMax:
                    rightMax = height[ptr2]
                else:
                    water+= rightMax-height[ptr2]
                ptr2-=1
        return water