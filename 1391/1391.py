class Solution:
    valid = False
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        valid_neighbor = [
            [],
            [[], [], [1,4,6], [1,3,5]],     # up, down, left, right
            [[2,3,4], [2,5,6], [], []],
            [[], [2,5,6], [1,4,6], []],
            [[], [2,5,6], [], [1,3,5]],
            [[2,3,4], [], [1,4,6], []],
            [[2,3,4], [], [], [1,3,5]]
        ]
        
        def dfs(x, y, m, n, grid, flag):
            if x==m-1 and y==n-1:
                self.valid = True
                return
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            for i in range(4):
                newx = x+dx[i]
                newy = y+dy[i]
                if not (newx>=0 and newx<m and newy>=0 and newy<n) or flag[newx][newy]==1:
                    continue
                # print([x,y], valid_neighbor[grid[x][y]])
                if grid[newx][newy] in valid_neighbor[grid[x][y]][i]:
                    flag[newx][newy] = 1
                    dfs(newx, newy, m, n, grid, flag)
                    flag[newx][newy] = 1
        
        self.valid = False
        flag = copy.deepcopy(grid)
        flag[0][0] = 1
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                flag[i][j] = 0
        dfs(0, 0, m, n, grid, flag)
        return self.valid