class ProductOfNumbers:

    def __init__(self):
        self.product = []
        self.preZero = []   # 记录了到第 i 个数为止，前面的0在哪个下标（包含i这个位置）
        self.numList = []
        self.nNumber = 0

    def add(self, num: int) -> None:        
        if self.nNumber == 0:       # 第一次插入
            self.product.append(num)
            self.preZero.append(0 if num==0 else -1)
        elif self.product[-1] == 0:     # 前面乘积为0
            self.product.append(num)
            self.preZero.append(self.preZero[-1] if num!=0 else self.nNumber)
        else:       # 正常插入
            self.product.append(num*self.product[-1])
            self.preZero.append(self.preZero[-1] if num!=0 else self.nNumber)
        
        self.numList.append(num)
        self.nNumber += 1
            

    def getProduct(self, k: int) -> int:
        # print(self.product)
        left = self.nNumber - k
        if self.preZero[self.nNumber-1] >= left:        # has a '0' in the sequence
            return 0
        return self.product[-1]//self.product[left]*self.numList[left]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)