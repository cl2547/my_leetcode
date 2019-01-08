class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.list = []
        self.size = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.list) >= self.size:
            self.list.pop(0)
        self.list.append(val)
        return sum(self.list)/len(self.list)
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)