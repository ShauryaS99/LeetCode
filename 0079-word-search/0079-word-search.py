class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #Technically O(mn & 4^L (length of word)) but realistically O(mn)
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        def dfs (node, visited, curr_str):
            visited.add(node)
            x, y = node
            
            curr_str += board[x][y]
            if curr_str == word:
                return True
            # Curr str has diverged
            if len(curr_str) > len(word) or curr_str != word[:len(curr_str)]:
                # Backtrack from neighbors
                visited.remove(node)
                return False
            
            # Add more letters
            for dx, dy in dirs:
                new_x = x + dx
                new_y = y + dy
                if (0 <= new_x < len(board)) and \
                (0 <= new_y < len(board[0])) and \
                ((new_x, new_y) not in visited):
                    if dfs((new_x, new_y), visited, curr_str):
                        return True
            
            # Backtrack parent node: all paths under this node are bad
            visited.remove(node)
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                # Must start with first letter of word
                if board[i][j] == word[0]:
                    found_word = dfs((i, j), set(), '')
                    if found_word:
                        return True
        
        return False