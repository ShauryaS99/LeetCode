class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #O(mn)
        if not board or not board[0]:
            return
        
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        def dfs(x, y):
            # Modify edge-connected cells to 'E'
            board[x][y] = 'E'
            for dx, dy in dirs:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < len(board) and \
                0 <= new_y < len(board[0]) and \
                board[new_x][new_y] == 'O':
                    dfs(new_x, new_y)
        
        # Start DFS from 'O's on the edges
        for i in range(len(board)):
            for j in range(len(board[0])):
                if ((i == 0 or i == len(board) - 1) or \
                (j == 0 or j == len(board[0]) - 1)) and \
                board[i][j] == 'O':
                    dfs(i, j)
        
        # Update the board
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'  # Flip surrounded 'O's
                elif board[i][j] == 'E':
                    board[i][j] = 'O'  # Restore edge-connected 'O's
