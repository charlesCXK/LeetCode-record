class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        
        def findMin(nums, target):
            left, right = 0, len(nums)-1
            if right == -1:
                return -1

            while left < right:
                mid = (left+right) // 2
                
                if nums[mid] > nums[right]:
                    left = mid+1
                else:
                    right = mid

            return left
        
        def binarySearch(nums, target):
            if len(nums) == 0:
                return -1

            left, right = 0, len(nums)-1
            while left < right:
                # print(left, right)
                mid = (left+right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid-1
                else:
                    left = mid+1
            if nums[left] == target:
                return left
            return -1
        
        minIndex = findMin(nums, target)
        
        # print(minIndex)

        if nums[minIndex] == target:
            return minIndex
        elif target>=nums[0] and minIndex!=0:
            return binarySearch(nums[:minIndex], target)
        else:
            ans = binarySearch(nums[minIndex:], target)
            if ans == -1:
                return ans
            return binarySearch(nums[minIndex:], target)+minIndex