class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        l = 0

        h = len(matrix) - 1


        row_ind = 0


        while l <= h:

            mid = l + ((h-l)//2)

            if target <= matrix[mid][-1] and target >= matrix[mid][0]:

                row_ind = mid
                break

            elif target > matrix[mid][-1]:

                l = mid + 1

            else:

                h = mid - 1


        l = 0

        h = len(matrix[0]) - 1

        target_row = matrix[row_ind]

        
        while l <= h:

            mid = l + ((h-l)//2)

            if target_row[mid] == target:

                return True

            elif target_row[mid] > target:

                h = mid - 1

            else:

                l = mid + 1

        return False