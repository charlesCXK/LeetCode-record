'''
If S==T, each letter's count in S should be the same as that of T's.
'''

class Solution:
    def numSpecialEquivGroups(self, A: 'List[str]') -> 'int':
        # calculate the feature of the str
        def feature(s):
            ans = [0] * 52
            for i, letter in enumerate(s):
                ans[ord(letter) - ord('a') + 26 * (i%2)] += 1
            return tuple(ans)
        
        word_features = [feature(word) for word in A]
        word_features = set(word_features)
        return len(word_features)