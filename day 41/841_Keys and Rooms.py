# LeetCode 841. Keys and Rooms
# Difficulty: Easy
# Topic: Graph, DFS

class Solution(object):
    def canVisitAllRooms(self, rooms):
        visited = set()

        def dfs(node):
            visited.add(node)

            for neighbour in rooms[node]:
                if neighbour not in visited:
                    dfs(neighbour)

        dfs(0)

        return len(visited) == len(rooms)