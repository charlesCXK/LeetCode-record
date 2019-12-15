class Solution:
    import copy
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m = len(mat)
        n = len(mat[0])
        
        colSum = copy.deepcopy(mat)             # sum of the column from (0,j) to (i,j)
        for i in range(1, m):
            for j in range(n):
                colSum[i][j] = mat[i][j] + colSum[i-1][j]
        
        matrixSum = copy.deepcopy(colSum)       # sum of the matrix from (0,0) to (i,j)
        for j in range(1, n):
            for i in range(m):
                matrixSum[i][j] = matrixSum[i][j-1] + colSum[i][j]
    
        # for line in mat:
        #     print(line)
        # print('********')
        # for line in matrixSum:
        #     print(line)
                
        maxSidelen, minLen, maxLen = 0, 0, min(m, n)
        # binary search the sidelen
        while minLen <= maxLen:
            sidelen = (minLen+maxLen) // 2
            flag = False
            
            for i in range(m+1-sidelen):
                if flag:
                    break
                for j in range(n+1-sidelen):
                    # calculate the sum of matrix[i:i+sidelen, j:j+sidelen] using the area of four rectangles.
                    if i > 0:
                        up = matrixSum[i-1][j+sidelen-1]
                    else:
                        up = 0
                    
                    if j > 0:
                        left = matrixSum[i+sidelen-1][j-1]
                    else:
                        left = 0
                    
                    if i>0 and j>0:
                        leftup = matrixSum[i-1][j-1]
                    else:
                        leftup = 0
                    
                    mysum = matrixSum[i+sidelen-1][j+sidelen-1] - left - up + leftup
                    # print(mysum, i, j, sidelen, left, up, leftup)
                    if mysum <= threshold:
                        maxSidelen = max(maxSidelen, sidelen)
                        flag = True
            if flag:
                minLen = sidelen+1
            else:
                maxLen = sidelen-1
                
        return maxSidelen
        
        