class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        ''' 
        Count how many mutations are need to be conducted 
        to convert src to dst. 
        '''
        def checkMutation(src, dst):
            change = 0
            for i in range(len(src)):
                if src[i] != dst[i]:
                    change += 1
            return change
        
        queue = []
        lenBank = len(bank)
        flag = [0 for i in range(lenBank)]
        
        queue.append([start, 0])
        while len(queue) != 0:
            head = queue.pop(0)
            
            # find thesolution
            if head[0] == end:
                return head[1]
            
            for i in range(lenBank):
                # conduct one mutation
                if checkMutation(head[0], bank[i])==1 and flag[i]==0:
                    queue.append([bank[i], head[1]+1])
                    flag[i] = 1
        return -1