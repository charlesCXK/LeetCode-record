class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        num_list = []
        while n>0:
            num_list.append(n%10)
            n = n//10
        product, sum_ = 1, 0
        for ele in num_list:
            product *= ele
            sum_ += ele
        return product-sum_