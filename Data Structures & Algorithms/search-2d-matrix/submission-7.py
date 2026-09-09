class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        leftRow = 0
        rightRow = len(matrix) - 1

        while leftRow <= rightRow:

            med = (leftRow + rightRow) // 2

            if matrix[med][0] <= target and matrix[med][-1] >= target:

                left = 0
                right = len(matrix[0]) - 1

                while left <= right:

                    median = (left + right) // 2

                    if matrix[med][median] == target:
                        return True

                    elif matrix[med][median] > target:
                        right = median - 1

                    else:
                        left = median + 1

                return False

            elif matrix[med][0] > target:
                rightRow = med - 1

            else:
                leftRow = med + 1

        return False