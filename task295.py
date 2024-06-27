from heapq import heapify, heappop, heappush
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if self.left and num > -self.left[0]: heappush(self.right, num)
        else: heappush(self.left, -num)
        if len(self.left) - len(self.right) == 2: heappush(self.right, -heappop(self.left))
        if len(self.right) - len(self.left) == 2: heappush(self.left, -heappop(self.right))

    def findMedian(self) -> float:
        if len(self.left) == len(self.right): return (self.right[0] - self.left[0]) / 2.0
        elif len(self.left) > len(self.right): return -self.left[0]
        else: return self.right[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# Follow up: 
# If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution? --> create a list of 100, counting the number of times each integer occurs
# If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution? --> a list of 100 + a hashmap
# what if the dataset is so large? --> use approximation algorithm like TDigest