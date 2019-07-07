class Solution:
    def mySqrt(self, x: int) -> int:
        # find the largest number who is smaller than sqrt(x)  
        left = 0
        right = x
        while left < right:
            mid = (left+right) // 2
            if mid**2 > x:
                right = mid-1
            elif mid**2 <= x:
                if (mid+1)**2 > x:
                    return mid
                else:
                    left = mid+1
        return left