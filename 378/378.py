'''
Runtime: 56 ms, faster than 86.28% of Python3 online submissions
'''

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        
        # calculate how many elements less than v
        def countLE(v):
            res, right = 0, n-1
            flag = False
            for i in range(m):
                if right < 0:
                    break
                while right>=0 and matrix[i][right]>v:
                    right -= 1
                if matrix[i][right] == v:       # this element has shown in the matrix
                    flag = True
                res += (right+1)
            return res, flag
                
                
        # we want to find the first element that the number of the elements not larger than it is K.
        left, right = matrix[0][0], matrix[m-1][n-1]
        while left < right:
            mid = (left+right) // 2
            count, flag = countLE(mid)
            if count == k:
                if flag == False:       # This number is not in the matrix
                    right = mid-1
                else:
                    return mid
            elif count > k:
                right = mid
            elif count < k:
                left = mid+1

        return right