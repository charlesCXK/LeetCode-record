'''
当考虑 a,[b,...c],d 时，想翻转 [b,c] 之间的数字，那么翻转之后的 gap 为 2* {min(c,d)-max(a,b)}。
这是很显然的，以 [a,b] 与 [c, d] 区间不相交为例，交换之后的gap其实是两个区间中间那部分的两倍。
注意考虑特殊情况：从第一位开始翻转或翻转到最后一位
'''
class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        n = len(nums)
        rawSum, maxSum = 0, 0
        for i in range(n-1):
            rawSum += abs(nums[i]-nums[i+1])
            
        low, high = math.inf, -math.inf
        for i in range(n-1):
            low = min(max(nums[i], nums[i+1]), low)
            high = max(min(nums[i], nums[i+1]), high)
        
        '''
        Special case.
        '''
        sp = 0
        for i in range(n-1):
            # flip [0, i]
            sp = max(sp, abs(nums[0]-nums[i+1])-abs(nums[i]-nums[i+1]))
            # flip [i, -1]
            sp = max(sp, abs(nums[-1]-nums[i-1])-abs(nums[i]-nums[i-1]))
                             
        
        return rawSum + max((high-low)*2, sp)