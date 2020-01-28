class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        '''
        分治算法
        '''
        char2int = collections.defaultdict(int)
        for c in s:
            char2int[c] += 1
        
        start = -1
        parts = []
        for i in range(len(s)):
            if char2int[s[i]]<k and start!=i:
                if start == -1:
                    start = 0
                parts.append(s[start:i])
                start = i+1
        
        if start == -1:
            return len(s)
        # append the last substring
        if start <= len(s):
            parts.append(s[start:])
        if len(parts) == 1:     # has reached the boundary case
            return len(parts[0])
        
        maxLength = 0
        for part in parts:
            maxLength = max(maxLength, self.longestSubstring(part, k))
            
        return maxLength