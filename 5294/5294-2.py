class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        curKey = set([i for i in initialBoxes if status[i]])
        curBox = set(initialBoxes)
        res = set()
        while curBox and curKey:
            open_box = curBox & curKey
            res |= open_box
            curBox -= open_box
            curKey -= open_box
            for b in open_box:
                curKey |= set([i for i in containedBoxes[b] if status[i]])
                curBox |= set(containedBoxes[b])
                curKey |= set(keys[b])
        return sum([candies[i] for i in res])