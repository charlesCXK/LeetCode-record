class Solution:
    maximumCandies = 0
    nowCandies = 0
    
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        def dfs(nowIdx):
            # I haven't take the candies in this box
            if self.flag[nowIdx] == 0:
                self.nowCandies = self.nowCandies + candies[nowIdx]
                self.flag[nowIdx] = 1
            else:
                return
            
            # collect all the keys
            for key in keys[nowIdx]:
                self.mykeys[key] = 1
                # use the new collected keys to open the unopened boxes
                if key in self.unopenedBox:
                    self.unopenedBox.remove(key)
                    dfs(key)
            
            # these boxes are not opened yet
            for idx in containedBoxes[nowIdx]:
                self.unopenedBox.append(idx)
                
            for box in self.unopenedBox:
                if self.mykeys[box]==1 or status[box]==1:
                    self.unopenedBox.remove(box)
                    dfs(box)
                    
        lenStatus = len(status)
        self.maximumCandies = 0
        self.nowCandies = 0
        self.mykeys = [0 for i in range(lenStatus)]
        self.flag = [0 for i in range(lenStatus)]
        self.unopenedBox = []
        
        for startIdx in initialBoxes:
            dfs(startIdx)
        
        return self.nowCandies