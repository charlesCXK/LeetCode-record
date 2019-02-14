'''
这是直方图最大矩形面积的模板题。首先，联系到木桶的短板效应，即木桶最多能装的水的数量，由最短那块木板决定。
那么同理，如果想要在直方图中得到最大矩形面积，这个矩形的高度至少可以撑满一个bar(一个bar指直方图中一个竖条)。
因为如果没有撑满任何bar的话，向上扩大一点点直到撑满某个bar的高度，可以得到更大的矩形。

既然肯定会撑满某个bar，那么问题可以转化为，找到某个bar，以它的高度作为矩形的高度，看以它为中心向左右扩散，
最大能得到多大的矩形。暴力枚举容易超时，这里介绍维护单调栈的算法。

这里以一个stack模拟一个单调栈，里面存放bar的下标，按照bar的高度是非严格递增的。
然后在直方图最开始和最末尾各加入一个高度为0的 bar，方便处理边界值。

处理当前下标为 i 的bar。
一、当栈为空时，直接将下标 i 压入栈中。
二、当栈内有元素时，如果栈顶元素不高于 heights[i]，直接将 i 压入栈中；
否则，假设栈顶元素是 top，对应的 bar 的高度是 heights[top]。将此元素弹出栈，此时栈顶元素假定为 tmp_top，然后可以得到一个显然的性质：
下标 tmp_top 到下标 i 之间的所有 bar 的高度，都不低于 heights[top]。分两步证明：

1. 假设 top~i 之间有 bar 的高度小于 heights[top]，那么 top 这个元素会被弹出栈，不应该存在。
2. 假设 tmp_top~top 之间有 bar 的高度小于 heights[top]，那么不满足栈的单调性，显然不成立，得证。
然后下标 tmp_top 到下标 i 之间的所有 bar，可以组成一个高度为 heights[top] 的矩形。面积为 heights[top] * (i-tmp_top-1)。
与当前记录的最大面积比较并更新即可。
'''


class Solution:
    def largestRectangleArea(self, heights: 'List[int]') -> 'int':
        heights = [0] + heights + [0]
        stack = []
        area = 0
        
        for i in range(0, len(heights)):
            if len(stack) == 0:
                stack.append(i)
            else:
                while len(stack)>0 and heights[stack[-1]]>heights[i]:
                    top = stack.pop()
                    area = max(area, (i-stack[-1]-1)*heights[top])
                stack.append(i)
        return area
            
                    