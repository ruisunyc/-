import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_h = []
        self.min_h = []

    def addNum(self, num: int) -> None:
        if len(self.max_h)==len(self.min_h):
            heapq.heappush(self.min_h,-heapq.heappushpop(self.max_h,-num)) #�󶥶����ֵѹ��С����
        else:
            heapq.heappush(self.max_h,-heapq.heappushpop(self.min_h,num)) #С������Сֵѹ��󶥶�

    def findMedian(self) -> float:        
        if len(self.max_h)!=len(self.min_h):
            return self.min_h[0]
        else:
            return (-self.max_h[0]+self.min_h[0])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()