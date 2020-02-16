class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        right = n
        ret = 0
        
        for i in range(m):
            for j in range(n):
                if j >= right:
                    break
                if grid[i][j] < 0:
                    ret += (right-j)*(m-i)
                    right = j
        return ret