from collections import defaultdict
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        #O(n)
        team_score = {} # team: incoming edges (teams that are strong than them)
        for i in range(n):
            team_score[i] = 0
        for a, b in edges:
            team_score[b] += 1
        
        least_teams_stronger = len(edges)
        strong_teams = []
        # Get strongest team (team w/ lowest dict value)
        for team, stronger_teams in team_score.items():
            if stronger_teams < least_teams_stronger:
                least_teams_stronger = stronger_teams
                strong_teams = [team]
            # In case of ties, keep both teams in list
            elif stronger_teams == least_teams_stronger:
                strong_teams.append(team)
                
        # If there are ties, return -1
        if len(strong_teams) > 1:
            return -1
        else:
            return strong_teams[0]
        