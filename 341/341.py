'''
Runtime: 68 ms, faster than 75.44% of Python online submissions
'''

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.lst = self.constructLst(nestedList)
        self.len = len(self.lst)
        self.ind = 0
    
    def constructLst(self, item):
        ret = []
        for ele in item:
            ret += self.dfsTraversal(ele)
        return ret
    
    '''
    Recursively build the list.
    '''
    def dfsTraversal(self, item):
        if item.isInteger():
            return [item.getInteger()]
        else:
            retLst = []
            for ele in item.getList():
                retLst += self.dfsTraversal(ele)
            return retLst
        

    def next(self):
        """
        :rtype: int
        """
        val = self.lst[self.ind]
        self.ind += 1
        return val
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.ind < self.len
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())