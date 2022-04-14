# the bottle neck is finding the max/min/current
# SortedList is introduced to mantain max/min
# self.cur is introduced to maintain current
from sortedcontainers import SortedList
class StockPrice:
    def __init__(self):
        self.record = {}
        self.price = SortedList()
        self.cur = 0

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.record:
            self.price.discard(self.record[timestamp])
        self.price.add(price)
        self.record[timestamp] = price
        self.cur = max(self.cur, timestamp)

    def current(self) -> int:
        return self.record[self.cur]

    def maximum(self) -> int:
        return self.price[-1]

    def minimum(self) -> int:
        return self.price[0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()