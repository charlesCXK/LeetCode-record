class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lastLessThan(nums, target):
            ''' 找到最后一个比 target 小的 '''
            if target <= nums[0]:
                return -1
            left, right = 0, len(nums)-1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    if nums[mid+1] >= target:
                        return mid
                    else:
                        left = mid+1
            return left
        
        def firstLargerThan(nums, target):
            ''' 找到第一个比 target 大的 '''
            if target >= nums[-1]:
                return -1
            left, right = 0, len(nums)-1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    if nums[mid-1] <= target:
                        return mid
                    else:
                        right = mid-1
            return left
        
        if len(nums) == 0:
            return [-1, -1]
        
        lth = lastLessThan(nums, target)
        flt = firstLargerThan(nums, target)
        
        left, right = -1, -1
        if lth == len(nums)-1:
            left = -1
        else:
            if nums[lth+1] == target:
                left = lth+1
        if flt == -1:
            if nums[-1] == target:
                right = len(nums) - 1
        else:
            if nums[flt-1] == target:
                right = flt-1
        return [left, right]