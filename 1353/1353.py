class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        from functools import cmp_to_key
        
        def mycmp(a, b):
            return a[1]-b[1] if a[1]!=b[1] else a[0]-b[0]
        
        events.sort(key=cmp_to_key(mycmp))
        workDay = []
        flag = [0 for i in range(100001)]
        
        for s,e in events:
            if flag[s] == 0:
                workDay.append(s)
                flag[s] = 1
            else:
                for day in range(s+1, e+1):
                    if flag[day] == 0:
                        flag[day] = 1
                        workDay.append(day)
                        break
        return len(workDay)

#         # print(events)
#         flag = [0 for i in range(100001)]
        
#         finishTime = events[0][0] + 1
#         flag[finishTime-1] = 1
#         ret = 1
#         for i in range(1, len(events)):
#             # print(finishTime, i)
#             if finishTime<=events[i][1]:
#                 ret += 1
#                 finishTime = max(finishTime, events[i][0]) + 1
#                 flag[finishTime-1] = 1
#             else:
#                 for j in range(events[i][0], events[i][1]+1):
#                     if flag[j] == 0:
#                         ret += 1
#                         finishTime = max(finishTime, events[i][0]) + 1
#                         flag[finishTime-1] = 1
        return ret