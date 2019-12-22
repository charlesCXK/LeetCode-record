class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ret = 0
        for ele in nums:
            if len(str(ele)) % 2 == 0:
                ret += 1
        return ret
        