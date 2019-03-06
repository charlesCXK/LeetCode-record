'''
Runtime: 40 ms, faster than 63.49% of Python3 online submissions
'''
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        numsSet = set()
        for n in nums:
            numsSet.add(n)
        nums = []
        for n in numsSet:
            nums.append(n)
        nums.sort(reverse=True)
        if len(nums) >= 3:
            return nums[2]
        else:
            return nums[0]