class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        groups = {}
        result = []
        for id, group in enumerate(groupSizes):
            if group in groups:
                groups[group].append(id)
            else:
                groups[group] = [id]
                
        for group in groups:
            group_size = int(group)
            for i in range(0, len(groups[group]), group_size):
                result.append(groups[group][i:i+group_size])
            
        return result