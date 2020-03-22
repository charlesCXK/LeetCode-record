class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def divisor_num(n):
            divisor = 0
            divisor_list = []
            for i in range(1, math.ceil(math.sqrt(n))):
                if n%i == 0:
                    divisor += 1
                    divisor_list.append(i)
                    divisor_list.append(n//i)
                if divisor > 2:
                    break
            divisor *= 2
            if math.ceil(math.sqrt(n)) == math.sqrt(n):     # this is important
                divisor += 1
            return divisor, divisor_list
    
        ret = 0
        for n in nums:
            d, l = divisor_num(n)
            # print(n, d)
            if d == 4:
                # print(l)
                ret += sum(l)
        return ret
        