class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        
        def calc_mask(s):
            return ''.join(sorted(s))
        for s in strs:
            mask = calc_mask(s)
            if mask in group:
                group[mask].append(s)
            else:
                group[mask] = [s]
        return list(group.values())