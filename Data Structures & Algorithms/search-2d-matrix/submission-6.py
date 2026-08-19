class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l, r = 0, len(matrix) - 1
        foundRow = False

        while l <= r and foundRow == False:
            mRow = l + ((r - l) // 2)

            if target >= matrix[mRow][0] and target <= matrix[mRow][-1]:
                foundRow = True
            elif target < matrix[mRow][0]:
                r = mRow - 1
            else:
                l = mRow + 1
        
        if not foundRow:
            return False
        
        print(f'Target is in row {mRow}')
        
        l, r = 0, len(matrix[mRow]) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if matrix[mRow][m] == target:
                return True
            elif matrix[mRow][m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return False



        