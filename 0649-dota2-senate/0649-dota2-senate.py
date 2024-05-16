class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque([i for i in range(len(senate)) if senate[i] == "R"])
        dire = deque([i for i in range(len(senate)) if senate[i] == "D"])
        
        # 2 queue approach O(N)
        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()
            if r < d:
                radiant.append(r + len(senate))
            else:
                dire.append(d + len(senate))
        if radiant:
            return "Radiant"
        else:
            return "Dire"
                        
            