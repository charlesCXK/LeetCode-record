'''
https://blog.csdn.net/pku_Coder/article/details/87379426
'''
class Solution:
    '''
    calculate the max area in the histogram
    '''
    def largestRectangInHistogram(self, row):
        heights = [0] + row + [0]
        stack = []
        max_area = 0
        
        for i in range(len(heights)):
            if len(stack) == 0:
                stack.append(i)
            else:
                while len(stack)>0 and heights[stack[-1]] > heights[i]:
                    top = stack.pop()
                    max_area = max(max_area, heights[top] * (i-stack[-1]-1))
                stack.append(i)
        return max_area
    
    def maximalRectangle(self, matrix: 'List[List[str]]') -> 'int':
        rows = len(matrix)
        max_area = 0
        
        if rows > 0:
            cols = len(matrix[0])
        else:
            return 0
        
        # heights[i]: Number of consecutive '1' above matrix[i][j] (including matrix[i][j])
        heights = [0 for i in range(cols)]
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    heights[j] = heights[j] + 1
                else:
                    heights[j] = 0
            max_rectangle_this_row = self.largestRectangInHistogram(heights)
            max_area = max(max_area, max_rectangle_this_row)    
                
        return max_area
        