class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        num_rooms = len(rooms)
        # For each room, go to the rooms it unlocks (skipping visited)
        def dfs(visited, room_num):
            visited.add(room_num)
            key_lst = rooms[room_num]
            for key in key_lst:
                if key in visited:
                    continue
                dfs(visited, key)
        dfs(visited, 0)
        # If we have visited each room: great!
        return len(visited) == num_rooms