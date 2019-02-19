'''
Runtime: 252 ms, faster than 87.65% of Python3 online submissions

for grid[i][j] and its neighbours, if its neighbour is zero, perimeter + 1.
'''

class Solution:
    def islandPerimeter(self, grid: 'List[List[int]]') -> 'int':
        try:
            w, h = len(grid), len(grid[0])
        except:     # empty grid
            return 0
        
        new_grid = []
        perimeter = 0
        
        # add some zeros arround the grid
        new_grid.append([0 for i in range(h+2)])
        for i in range(w):
            new_grid.append([0] + grid[i] + [0])
        new_grid.append([0 for i in range(h+2)])
        
        for i in range(w+2):
            for j in range(h+2):
                if new_grid[i][j] == 1:
                    perimeter += (4-new_grid[i-1][j]-new_grid[i+1][j]-new_grid[i][j-1]-new_grid[i][j+1])
        return perimeter
                    