class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        clockwise rotate
        first reverse up to down, then swap the symmetry 
        1 2 3     7 8 9     7 4 1
        4 5 6  => 4 5 6  => 8 5 2
        7 8 9     1 2 3     9 6 3
        
        anticlockwise rotate
        first reverse left to right, then swap the symmetry
        1 2 3     3 2 1     3 6 9
        4 5 6  => 6 5 4  => 2 5 8
        7 8 9     9 8 7     1 4 7
        """
        # Flip matrix vertically (only top half of rows)
        for row in range(len(matrix) // 2):
            for col in range(len(matrix[0])):
                top_val = matrix[row][col]
                bottom_row = (len(matrix) - 1) - row
                bottom_val = matrix[bottom_row][col]
                matrix[row][col] = bottom_val
                matrix[bottom_row][col] = top_val
        
        # Swap x & y (only upper right triangle of matrix)
        for row in range(len(matrix)):
            for col in range(row + 1, len(matrix[0])):
                og_val = matrix[row][col]
                new_val = matrix[col][row]
                matrix[row][col] = new_val
                matrix[col][row] = og_val
        