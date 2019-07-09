class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        if right == -1:
            return None
        
        while left < right:
            print(left, right)
            mid = (left+right) // 2
            
            if nums[mid] > nums[mid+1]:     # 这个数比后面大，最小值肯定不是这个数
                left = mid+1
            elif nums[mid] < nums[mid-1]:       # 这个数比前面的小，直接返回
                return nums[mid]
            else:
                if nums[mid] > nums[right]:     # 他比最右边大，最小值在右边
                    left = mid + 1
                else:
                    right = mid-1
                
        return nums[left]