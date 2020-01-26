class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        edge = [[math.inf for i in range(n)] for j in range(n)]
        for e in edges:
            edge[e[0]][e[1]] = e[2]
            edge[e[1]][e[0]] = e[2]
    
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if edge[i][k]+edge[k][j] < edge[i][j]:
                        edge[i][j] = edge[i][k]+edge[k][j]
        
        minId, minCityNum = -1, math.inf
        
        for i in range(n):
            neighbor = 0
            for j in range(n):
                if j != i:
                    if edge[i][j] <= distanceThreshold:
                        neighbor += 1
            # print(neighbor)
            if neighbor <= minCityNum:
                minCityNum = neighbor
                minId = i
        return minId