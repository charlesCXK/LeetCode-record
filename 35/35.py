class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        if target > nums[-1]:
            return len(nums)
        elif target < nums[0]:
            return 0
        while left < right:
            mid = (left+right) // 2
            print(nums[mid])
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                if nums[mid-1] >= target:
                    right = mid - 1
                else:
                    return mid
            else:
                if nums[mid+1] > target:
                    return mid+1
                else:
                    left = mid + 1
        return left
        