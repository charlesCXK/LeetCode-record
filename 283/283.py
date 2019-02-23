class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        it = 0
        while it < len(nums):
            while it<len(nums) and nums[it] == 0:
                nums.pop(it)
            it += 1
        for i in range(length-len(nums)):
            nums.append(0)