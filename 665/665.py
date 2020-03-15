class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        cnt = 0
        
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                if i == 1:
                    cnt += 1
                else:       # change nums[i] or change nums[i-1]
                    if nums[i] >= nums[i-2]:        # [3,6,4,5]
                        cnt += 1
                        nums[i-1] = nums[i-2]
                    else:
                        nums[i] = nums[i-1]
                        cnt += 1
        return cnt<=1