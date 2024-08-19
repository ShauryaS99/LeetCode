from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #O(n^2) because each word can enqueue all other words in the list
        
        # Convert to set b/c membership tests for sets are O(1), instead of O(n)
        set_wordList = set(wordList)
        if endWord not in set_wordList:
            return 0
        
        transforms = 0
        q = deque([(beginWord, 1)])
        # Optimization using 2 sets to reduce wordList space so we only keep words once in queue
        reduced_wordList = set_wordList.copy()
        
        # BFS, when we reach endword first: return depth
        while q:
            word, depth = q.popleft()
            
            if word == endWord:
                return depth
            
            # Get words with 1 letter difference
            set_wordList = reduced_wordList.copy()
            for w in set_wordList:
                diff_counter = 0
                for i in range(len(word)):
                    if w[i] != word[i]:
                        diff_counter += 1
                if diff_counter == 1:
                    q.append((w, depth + 1))
                    reduced_wordList.remove(w)
        
        return 0