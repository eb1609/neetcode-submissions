class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            med = (right + left) // 2
            if nums[med] > nums[right]:
                left = med + 1
            else:
                right = med
        pivot = left

        if pivot == 0:
            l, r = 0, len(nums) - 1          # not rotated: whole array is sorted
        elif nums[0] <= target <= nums[pivot - 1]:
            l, r = 0, pivot - 1
        else:
            l, r = pivot, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return -1