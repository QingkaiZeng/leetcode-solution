class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix or target is None:
            return False
        row, col = len(matrix), len(matrix[0])
        
        left, right = 0 , row*col - 1
        while left <= right:
            mid = (left + right) // 2
            num_buffer = matrix[mid // col][mid % col]
            if num_buffer < target:
                left  = mid + 1
            elif num_buffer > target:
                right = mid - 1
            else:
                return True
        return False