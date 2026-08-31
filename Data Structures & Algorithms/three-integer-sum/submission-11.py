class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i, n in enumerate(nums):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            ptr1 = i + 1
            ptr2 = len(nums) - 1
            target = -n

            while ptr1 < ptr2:

                total = nums[ptr1] + nums[ptr2]

                if target == total:
                    result.append([n, nums[ptr1], nums[ptr2]])

                    ptr1 += 1
                    ptr2 -= 1

                    while ptr1 < ptr2 and nums[ptr1] == nums[ptr1 - 1]:
                        ptr1 += 1

                    while ptr1 < ptr2 and nums[ptr2] == nums[ptr2 + 1]:
                        ptr2 -= 1

                elif target < total:
                    ptr2 -= 1

                else:
                    ptr1 += 1

        return result