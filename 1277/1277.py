class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = [] # dp[i][j] represents the maximum matrix it can form at position (i,j)
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            dp.append([])
            for j in range(cols):
                dp[i].append(matrix[i][j])
        
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    continue
                up, left = 0, 0
                up_left = dp[i-1][j-1]
                for k in range(i-1, i-2-up_left, -1):
                    if matrix[k][j] == 1:
                        up += 1
                    else:
                        break
                for k in range(j-1, j-2-up_left, -1):
                    if matrix[i][k] == 1:
                        left += 1
                    else:
                        break
            
                dp[i][j] = 1 + min(up_left, min(up, left))
        
        tot_num = 0
        for i in range(rows):
            for j in range(cols):
                tot_num += dp[i][j]

        return tot_num