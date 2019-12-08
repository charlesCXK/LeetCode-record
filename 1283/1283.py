class Solution:
    import math
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        flag = -1
        while left <= right:
            mid = (left+right) // 2
            tmp_sum = 0
            for ele in nums:
                tmp_sum += math.ceil(ele/mid)
            if tmp_sum > threshold:
                left = mid+1
            else:
                flag = mid
                right = mid-1
        return flag