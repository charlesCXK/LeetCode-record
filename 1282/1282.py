class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ret = []
        group_list = []
        group_index = []
        for i in range(len(groupSizes)+1):
            group_list.append([[]])
            group_index.append(0)
        for i,idx in enumerate(groupSizes):
            if len(group_list[idx][group_index[idx]]) < idx:
                group_list[idx][group_index[idx]].append(i)
            else:
                group_list[idx].append([i])
                group_index[idx] = group_index[idx]+1
        for i in range(len(group_list)):
            for list_ in group_list[i]:
                if len(list_) > 0:
                    ret.append(list_)
        print(group_list)
        return ret