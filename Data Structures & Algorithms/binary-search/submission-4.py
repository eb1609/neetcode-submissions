class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left<=right:
            med = (int)((right + left)/2)
            if nums[med]==target:
                return med
            elif nums[med]>target:
                right = med-1
            else:
                left = med+1
        return -1