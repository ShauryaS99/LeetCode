class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # O(n)
        if len(s1) > len(s2):
            return False
        
        # Create freq dicts
        s1_counts = {}
        s2_counts = {}
        for i in range(len(s1)):
            s1_counts[s1[i]] = s1_counts.get(s1[i], 0) + 1
            s2_counts[s2[i]] = s2_counts.get(s2[i], 0) + 1
        # Check if first k chars are permutations
        if s1_counts == s2_counts:
            return True
            
        l = 0
        # Fixed window
        while l + len(s1) < len(s2):
            # Decrement l char, and increment r char
            s2_counts[s2[l]] -= 1
            s2_counts[s2[l + len(s1)]] = s2_counts.get(s2[l + len(s1)], 0) + 1
            if s2_counts[s2[l]] == 0:
                del s2_counts[s2[l]]
                
            # If new window is equal return true
            if s1_counts == s2_counts:
                return True
            
            l += 1
        
        return False
                
        