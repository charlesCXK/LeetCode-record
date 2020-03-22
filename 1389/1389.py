class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        len_target = 0
        for i in range(len(nums)):
            if index[i] == len_target:
                target.append(nums[i])
                len_target += 1
            else:
                target = target[:index[i]] + [nums[i]] + target[index[i]:]
                len_target += 1
        return target