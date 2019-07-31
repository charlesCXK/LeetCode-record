class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        
        while n > 1:
            n -= 1
            news = ''
            len_s = len(s)
            it = 0
            
            cur_char, len_char = s[0], 1
            while it < len_s:
                if it == len_s-1:
                    news = news + str(len_char) + cur_char
                else:
                    if s[it+1] == s[it]:
                        len_char += 1
                    else:   # s[it] != s[it+1]
                        news = news + str(len_char) + cur_char
                        cur_char = s[it+1]
                        len_char = 1
                it += 1
            s = news
        return s