class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #RUntime: O(n^2)
        def validate_rows():
            for i in range(len(board)):
                lst = []
                for j in range(len(board[0])):
                    if board[i][j] != '.':
                        lst.append(board[i][j])
                if len(lst) != len(set(lst)):
                    return False
            return True
        
        def validate_cols():
            for col in range(len(board[0])):
                lst = []
                for row in range(len(board)):
                    if board[row][col] != '.':
                        lst.append(board[row][col])
                if len(lst) != len(set(lst)):
                    return False
            return True
        
        def validate_squares(row_min, row_max, col_min, col_max):
            lst = []
            for i in range(row_min, row_max):
                for j in range(col_min, col_max):
                    if board[i][j] != '.':
                        lst.append(board[i][j])
            if len(lst) != len(set(lst)):
                    return False
            return True
            
        
        if not validate_rows():
            print("Invalid Rows")
            return False
        if not validate_cols():
            print("Invalid Col")
            return False
        row_ranges = [(0,3),(3, 6),(6, 9)]
        col_ranges = [(0,3),(3, 6),(6, 9)]
        for row in row_ranges:
            for col in col_ranges:
                row_min = row[0]
                row_max = row[1]
                col_min = col[0]
                col_max = col[1]
                if not validate_squares(row_min, row_max, col_min, col_max):
                    print(f"Invalid square: {row}:{col}")
                    return False
        return True
        
        