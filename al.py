class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = []
        for i in range(len(rooms)) :
            visited.append(False)
        
        def dfs(key):
            visited[key] = True;
            for nextKey in rooms[key]:
                if not visited[nextKey] :
                    dfs(nextKey)
        dfs(0)
        
        if False in visited:
            return False
        else:
            return True
        
