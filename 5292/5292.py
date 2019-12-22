class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        maxnum = max(nums)
        lennum = len(nums)
        flag = [0 for i in range(maxnum+1)]
        for num in nums:
            flag[num] += 1
        nums = sorted(nums)
        print(nums)
        
        for i,num in enumerate(nums):
            if flag[num] > 0:
                if num+k-1 > maxnum:
                    return False
                # K Consecutive Numbers
                for j in range(num, num+k):
                    if flag[j] > 0:
                        flag[j] -= 1
                    else:
                        return False
        return True