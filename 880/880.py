class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        n = len(S)
        decoded_len = 0
        it = 0
        
        # 找到解码后比K长的下标。之后不用再解码
        while it < n:
            if S[it].isdigit():
                decoded_len *= int(S[it])
            else:
                decoded_len += 1
            if decoded_len >= K:    # don't need to decode any more
                break
            it += 1
        
        while it >= 0:  
            oldK = K
            
            # print('K:', K, 'it:', it, 'dec:', decoded_len)
            # 是数字，把数字的长度去掉，K做对应操作
            if S[it].isdigit():
                decoded_len  = decoded_len // int(S[it])
                if K > decoded_len:
                    if K%decoded_len == 0:
                        K = decoded_len
                    else:
                        K %= decoded_len
                it -= 1
                continue
            else:       # 是字母，直接长度-1
                if decoded_len == K:
                    return S[it]
                decoded_len -= 1
                if decoded_len < K:
                    K -= 1
    
            if K <= 0:
                return S[oldK-1]

            

            it -= 1
