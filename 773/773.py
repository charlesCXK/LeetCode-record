'''
Breadth-First Search
I don't know why in LeetCode, list.copy() is a deep copy?
For example, b = a.copy, then I modify some elements in b, the corresponding elements in 
a will be modified too. This bothers me!
'''

class Solution:
    visited = []
    
   # judge whether this list is the target list
    def judge(self, lst):
        for i in range(6):
            target = [1,2,3,4,5,0]
            if lst[i] != target[i]:
                return False
        return True
    
    # spread out the 2-d array
    def spread(self, lst):
        ret = []
        for i in range(2):
            for j in range(3):
                ret.append(lst[i][j])
        return ret
    
    # why I write this function? ... Because in LeetCode, something is wrong with list.copy()
    def mycopy(self, lst):
        ret = []
        for i in range(len(lst)):
            ret.append([])
            for j in range(len(lst[i])):
                ret[i].append(lst[i][j])
        return ret
    
    # one step
    def move(self, lst, x, y):
        board, ret = [], []
        board.append(lst[:3])
        board.append(lst[3:])
        # up -> bottom
        if x == 0:
            b = self.mycopy(board)#.copy()
            # print(board)
            b[x][y], b[x+1][y] = b[x+1][y], 0
            ret.append([self.spread(b), x+1, y])
            del b
        # bottom -> up
        if x == 1:
            b = self.mycopy(board)#.copy()
            # print(123, board)
            b[x][y], b[x-1][y] = b[x-1][y], 0
            # print(13, board)
            ret.append([self.spread(b), x-1, y])
            del b
        # right -> left
        if y != 0:
            b = self.mycopy(board)#.copy()
            # print(board)
            b[x][y], b[x][y-1] = b[x][y-1], 0
            ret.append([self.spread(b), x, y-1])
            del b
        # left -> right
        if y != 2:
            b = self.mycopy(board)#.copy()
            # print(board)
            b[x][y], b[x][y+1] = b[x][y+1], 0
            ret.append([self.spread(b), x, y+1])
            del b
        return ret
            
            
    
    def slidingPuzzle(self, board: 'List[List[int]]') -> 'int':
        self.visited = []
        
        # gei the index of '0'
        for i in range(2):
            for j in range(3):
                if board[i][j] == 0:
                    x, y = i, j
                    break
        
        first_state = self.spread(board)
        myqueue = []
        myqueue.append([first_state, 0, x, y])
        self.visited.append(first_state)
        
        while len(myqueue) > 0:
            this_state = myqueue.pop(0)
            state, step, x, y = this_state[:]
            # has reached the target state
            if self.judge(state):
                return step
            possible_states = self.move(state, x, y)
            for s in possible_states:
                if s[0] not in self.visited:
                    myqueue.append([s[0], step+1, s[1], s[2]])
                    self.visited.append(s[0])
        return -1