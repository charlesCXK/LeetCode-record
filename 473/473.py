'''
We should divide the list into 4 subsets. Each subset has the same sum.
So for each element in the list, consider whether it belongs to the first
subset? the second subset?... etc. Depth-first Search.

Tip: It will be quicker if I sort the list.
'''

class Solution:
    flag = False
    
    def dfs(self, sbsum, width, lst, index):
        if index == len(lst):
            self.flag = True
            return
        if self.flag:
            return
            
        for i in range(4):
            if sbsum[i] + lst[index] <= width:
                sbsum[i] += lst[index]
                self.dfs(sbsum, width, lst, index+1)
                sbsum[i] -= lst[index]
    
    def makesquare(self, nums: 'List[int]') -> 'bool':
        totlength = sum(nums)
        if totlength%4!=0 or totlength<=0:
            return False
        # get the width of square
        width = totlength // 4
        if max(nums) > width:
            return False
        
        # It will get a TLE if I don't sort it
        nums.sort(reverse=True)
                
        self.flag = False
        sbsum = [0, 0, 0, 0]        # sum of each subset
        self.dfs(sbsum, width, nums, 0)
        
        return self.flag