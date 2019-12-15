class Solution:
    import copy
    minStep = 999999
    dp = []
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dirx = [1, 0, -1, 0]
        diry = [0, 1, 0, -1]
        dstx, dsty = m-1, n-1
        print(m, n)
        
        def dfs(x, y, nowStep, nowK, grid, flag):
            if x==dstx and y==dsty:     # it has reached the destination
                self.minStep = min(self.minStep, nowStep)
                return

            if nowStep >= self.minStep:
                return
            
            if nowK <= self.dp[x][y]:
                return
            self.dp[x][y] = max(self.dp[x][y], nowK)        # dp[i][j]: the max k ever when it reaches position (i, j)

            for i in range(4):
                newx = x+dirx[i]
                newy = y+diry[i]
                if newx>=0 and newx<m and newy>=0 and newy<n and flag[newx][newy]==0:
                    if grid[newx][newy] == 0:
                        flag[newx][newy] = 1
                        dfs(newx, newy, nowStep+1, nowK, grid, flag)
                        flag[newx][newy] = 0
                    else:
                        if nowK >= 1:
                            flag[newx][newy] = 1
                            dfs(newx, newy, nowStep+1, nowK-1, grid, flag)
                            flag[newx][newy] = 0
                
        self.minStep = 999999
        flag = copy.deepcopy(grid)
        for i in range(len(flag)):
            for j in range(len(flag[0])):
                flag[i][j] = 0
                
        self.dp = copy.deepcopy(grid)
        for i in range(len(self.dp)):
            for j in range(len(self.dp[0])):
                self.dp[i][j] = -1
        
        
        dfs(0, 0, 0, k, grid, flag)
        if self.minStep != 999999:
            return self.minStep
        return -1