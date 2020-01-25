'''
O(n^2), TLE
'''

class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        n = len(nums)
        rawSum, maxSum = 0, 0
        for i in range(n-1):
            rawSum += abs(nums[i]-nums[i+1])
        
        for left in range(n):
            for right in range(left+1, n):
                delta = 0
                if left >= 1:
                    delta += (abs(nums[left-1]-nums[right]) - abs(nums[left-1]-nums[left]))
                if right+1 < n:
                    delta += (abs(nums[left]-nums[right+1]) - abs(nums[right]-nums[right+1]))
                maxSum = max(maxSum, delta+rawSum)
        return maxSum
                