class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left<right:
            med = (right+left)//2
            if nums[med]>nums[right]:
                left = med+1
            else:
                right = med
        return nums[left]

