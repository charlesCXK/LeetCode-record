class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_area = 0
        self.area = 1

        def dfs(x, y, flag, grid):
            dx = [-1, 1, 0, 0]
            dy = [0, 0, 1, -1]
            for i in range(4):
                newx = x+dx[i]
                newy = y+dy[i]
                if newx>=0 and newx<m and newy>=0 and newy<n and flag[newx][newy]==0 and grid[newx][newy]==1:
                    flag[newx][newy] = 1
                    self.area += 1
                    dfs(newx, newy, flag, grid)
                    
        flag = copy.deepcopy(grid)
        for i in range(m):
            for j in range(n):
                flag[i][j] = 0
        
        for i in range(m):
            for j in range(n):
                if flag[i][j]==0 and grid[i][j]==1:
                    flag[i][j] = 1
                    self.area = 1
                    dfs(i, j, flag, grid)
                    max_area = max(max_area, self.area)
        return max_area