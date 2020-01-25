class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        startRow = [0 for i in range(n-1)] + [i for i in range(m)]
        startCol = [i+1 for i in range(n-1)] + [0 for i in range(m)]
        
        for i in range(m+n-1):
            unsorted = []
            row, col = startRow[i], startCol[i]
            while row<m and col<n:
                unsorted.append(mat[row][col])
                row += 1
                col += 1
            row, col = startRow[i], startCol[i]
            
            unsorted.sort()
            it = 0
            while row<m and col<n:
                mat[row][col] = unsorted[it]
                row += 1
                col += 1
                it += 1
        return mat