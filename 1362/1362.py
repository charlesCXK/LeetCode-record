class Solution:
    res = 0
    def closestDivisors(self, num: int) -> List[int]:
        # 质因数分解
        def primeDivide(n):
            k = 2
            rawn = n
            mid = int(math.sqrt(n))+1       # 只处理到根号即可
            ret = []
            while k<=mid:
                if n%k == 0:
                    ret.append(k)
                    n //= k
                else:
                    k += 1

            check = 1
            for e in ret:
                check *= e
            if rawn%check == 0:
                if rawn == check:
                    return ret
                else:
                    ret.append(rawn//check)     # 处理最后一个引子
                    return ret
            else:
                return [1, rawn]
        
        primes1 = primeDivide(num+1)
        primes2 = primeDivide(num+2)
        
        # print(primes1, primes2)
        
        # 枚举法，确定最适合的乘积
        def dfs(idx, target, nowproduct, lst):
            # print(nowproduct, lst)
            if idx == len(lst):
                if abs(target-nowproduct)<abs(self.res-target):
                    self.res = nowproduct
                return
            dfs(idx+1, target, nowproduct*lst[idx], lst)
            dfs(idx+1, target, nowproduct, lst)
        
        dfs(0, math.sqrt(num+1), 1, primes1)
        ret1 = [self.res, (num+1)//self.res]
        self.res = 0
        dfs(0, math.sqrt(num+2), 1, primes2)
        ret2 = [self.res, (num+2)//self.res]
        
        # print(ret1, ret2)
        
        if abs(ret1[1]-ret1[0]) < abs(ret2[0]-ret2[1]):
            return ret1
        return ret2