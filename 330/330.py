'''
Runtime: 44 ms, faster than 57.78% of Python3

nums = [1, 2, 4, 13, 43]
贪心法。考虑到当前第 i 个数nums[i]( i 从1开始)，目前所有的和为 sum1。
1. 若第 i+1 个数 nums[i+1] 大于 sum1 + 1，那么前 i 个数无法组合成区间 [1:nums[i+1]) 的所有数字，需要插入一个数字: sum1 + 1;
2. 若第 i+1 个数 nums[i+1] 不大于 sum1 + 1，那么前 i 个数可以组合成区间 [1:sum1 + nums[i+1]) 的所有数字，继续考虑下面。
'''

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        nowSum, addNum = 0, 0
        
        # Must have '1' in the list
        if len(nums)==0 or nums[0]!=1:
            nums = [1] + nums
            addNum += 1
            
        for i, element in enumerate(nums):
            nowSum += nums[i]
            if nowSum >= n:
                return addNum
            
            if i!=len(nums)-1 and nums[i+1]>nowSum+1:
                # keep adding number until the condition is satisfied
                while nowSum+1<nums[i+1]:
                    if nowSum >= n:
                        return addNum
                    nowSum = 2*nowSum+1
                    addNum += 1
        
        while nowSum < n:
            nowSum = 2*nowSum+1
            addNum += 1
        return addNum