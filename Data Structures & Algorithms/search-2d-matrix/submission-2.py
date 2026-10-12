class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo = 0
        hi = len(matrix[0]) - 1
        row = -1
        
        for i in range(len(matrix)):
            if (target >= matrix[i][lo] and target <= matrix[i][hi]):
                if (target == matrix[i][lo] or target == matrix[i][hi]):
                    return True
                row = i
                break

        if row == -1:
            return False

        while (lo <= hi):
            mid = int(lo + (hi-lo)/2)
            val = matrix[row][mid]
            if val == target:
                return True
            elif val < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return False