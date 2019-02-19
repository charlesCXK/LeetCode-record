'''
If a node's out degree is 0, it is a terminal node.
Delete it from the graph, and delete its in-edges.
Do this iteratively until there is no node whose out degree is 0.
'''

class Solution:
    def eventualSafeNodes(self, graph: 'List[List[int]]') -> 'List[int]':
        nodenum = len(graph)        # number of nodes
        myqueue, ret = [], []        # store nodes whose out-degree is 0
        innode = [[] for i in range(nodenum)]
        outdegree = [0 for i in range(nodenum)]
        
        for i in range(nodenum):
            for node in graph[i]:
                outdegree[i] += 1
                innode[node].append(i)
        # node whose out degree is 0
        for i in range(nodenum):
            if outdegree[i] == 0:
                myqueue.append(i)
        
        while len(myqueue):
            thisnode = myqueue.pop(0)
            ret.append(thisnode)
            # delete this node, delete its in edges
            for node in innode[thisnode]:
                outdegree[node] -= 1
                if outdegree[node] == 0:
                    myqueue.append(node)
        ret.sort()
        return ret
                
        
                
        