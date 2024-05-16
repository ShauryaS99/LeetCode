class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate_lst = list(senate)
        victory = False
        # Time complexity O(n^2)
        while not victory:
            s = 0
            while s < len(senate_lst):
                next_s = (s + 1) % len(senate_lst)
                # Radiant senator will block the next Dire
                if senate_lst[s] == "R":
                    while senate_lst[next_s] != "D":
                        # No remaining Dire
                        if next_s == s:
                            return "Radiant"
                        next_s += 1
                        if next_s >= len(senate_lst):
                            next_s = next_s % len(senate_lst)
                    senate_lst[next_s] = 0
                # Dire senator will block the next Radiant
                elif senate_lst[s] == "D":
                    while senate_lst[next_s] != "R":
                        # No remaining Radiant
                        if next_s == s:
                            return "Dire"
                        next_s += 1
                        if next_s >= len(senate_lst):
                            next_s = next_s % len(senate_lst)
                    senate_lst[next_s] = 0
                s += 1
        return "Error"
                        
            