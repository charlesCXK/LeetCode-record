'''
动态规划
另 dp[i] 表示当前有 i 个节点时，所能产生的树的种类。
处理 n 个节点的情况时，遍历 1~n，另当前节点 root 作为根节点，然后 root 左侧节点一定比root小，
root 右侧节点一定比 root 大。左侧有 (root-1) 个节点，右侧有 (n-root) 个节点。那么以 root 为
根节点所产生树的种类为 dp[root-1] * dp[n-root]。遍历之后求和得出 dp[n]。
'''
class Solution:
    def numTrees(self, n: 'int') -> 'int':
        dp = [1 for i in range(n+1)]    # dp[i]: how many combinations when I have i nodes
        
        for root in range(1, n+1):  # compute dp[root]
            dp[root] = 0
            for i in range(1, root+1):
                left_node_num = i-1
                right_node_num = root-i
                dp[root] += dp[left_node_num] * dp[right_node_num]
        return dp[n]
        

'''
超时做法，递归构造左右子树
'''

'''
class Solution:
    def constructTree(self, lst):
        if len(lst) == 0:
            return 1
        
        # all node in the lst has ever been as a root
        tot_solution = 0
        
        for i in range(len(lst)):
            lefts = self.constructTree(lst[:i])
            rights = self.constructTree(lst[i+1:])
            
            # if this node is a root, how many solutions does it exist
            solution = lefts * rights
            tot_solution = tot_solution + solution
        
        return tot_solution
        
    def numTrees(self, n: 'int') -> 'int':
        lst = range(1, n+1)
        return self.constructTree(lst)
'''