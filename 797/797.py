'''
Runtime: 160 ms, faster than 45.13% of Python3 online submissions 
'''

class Solution:
    solution = []
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(vis, graph, nowPath):
            if nowPath[-1] == len(graph)-1:
                self.solution.append(nowPath.copy())
                return
            nownode = nowPath[-1]
            for node in graph[nownode]:
                if vis[node] == -1:
                    vis[node] = 1
                    nowPath.append(node)
                    dfs(vis, graph, nowPath)
                    vis[node] = -1
                    nowPath.pop(-1)
        
        n = len(graph)
        self.solution = []
        vis = [-1 for i in range(n)]
        vis[0] = 1
        dfs(vis, graph, [0])
        return self.solution
                    