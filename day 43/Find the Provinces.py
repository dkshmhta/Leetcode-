class Solution(object):
    def findCircleNum(self, isConnected):
        visited = set()
        provinces = 0

        def dfs(city):
            visited.add(city)

            for neighbor in range(len(isConnected)):
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    dfs(neighbor)

        for city in range(len(isConnected)):
            if city not in visited:
                provinces += 1
                dfs(city)

        return provinces