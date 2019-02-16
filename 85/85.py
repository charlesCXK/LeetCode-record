'''
将二维问题转化为一维求最长连续子序列的问题。对于第 i 行和第 j 行，求出 i 行到 j 行之间每一列的和，如果这个和等于 (j-i+1)，(说明这一列全为 1，可以成为矩阵的一个列)将这一列标记为1，否则将这一列标记为0。然后第 i 行到第 j 列其实形成了一个只包含 0 和 1 的一维数组。
在计算两行之间的列的和的时候，用动态规划算法提高速度。用一个数组 sumarray 记录某位置及该列以上所有元素的和。sumarray[i][j] = sum of matrix[0][j], matrix[1][j] … matrix[i][j]。然后求两行直接的列和的时候直接用 sumarray 做差即可。
--------------------- 
作者：PKU_CXK 
来源：CSDN 
原文：https://blog.csdn.net/pku_Coder/article/details/87379426 
'''

class Solution:
    '''
    给一个包含0和1的列表，求最长连续子序列
    '''
    def findMaxSequence(self, l: 'List[int]') -> 'int':
        length= len(l)
        max_length = 0
        if length == 0:
            return 0
        
        dp = [0 for i in range(length)]
        
        if l[0] == 1:
            dp[0] = 1
        
        for i in range(1, length):
            if l[i] == 1:
                if l[i-1] == 0:
                    dp[i] = 1
                else:
                    dp[i] = dp[i-1] + 1
            else:
                dp[i] = 0
        
        for i in range(length):
            max_length = max(max_length, dp[i])
        
        return max_length
    
    def maximalRectangle(self, matrix: 'List[List[str]]') -> 'int':
        rows = len(matrix)
        
        if rows > 0:
            cols = len(matrix[0])
        max_area = 0
        
        if rows==0 or cols==0:
            return 0
        
        # transfer it to an 'int' array
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = int(matrix[i][j])
        
        # sumarray[i][j]: sum of matrix[0][j], matrix[1][j] ... matrix[i][j]
        sumarray = matrix.copy()
        for i in range(1, rows):
            for j in range(cols):
                sumarray[i][j] = sumarray[i-1][j] + sumarray[i][j]
        
        for i in range(rows):
            for j in range(i, rows):
                if (j-i+1)*cols < max_area:
                    continue
                tmparray = []
                for k in range(cols):
                    if i == 0:
                        delta = sumarray[j][k]
                    else:
                        delta = sumarray[j][k] - sumarray[i-1][k]
                    
                    if delta == (j-i+1):
                        tmparray.append(1)
                    else:
                        tmparray.append(0)
                
                # pruning
                if sum(tmparray)*(j-i+1) < max_area:
                    continue
                    
                max_sequence = self.findMaxSequence(tmparray)
                max_area = max(max_area, max_sequence * (j-i+1))
                
        return max_area
        