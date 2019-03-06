'''
Runtime: 56 ms, faster than 22.64% of Python3 online submissions
'''
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1, max2, max3 = float("-inf"), float("-inf"), float("-inf")
        for n in nums:
            if n==max1 or n==max2 or n==max3:
                continue
            if n > max1:
                max1, max2, max3 = n, max1, max2
            elif n > max2:
                max2, max3 = n, max2
            elif n > max3:
                max3 = n

        if max3 != float("-inf"):
            return max3
        else:
            return max1