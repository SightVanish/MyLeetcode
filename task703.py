"""
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.
Implement KthLargest class:
KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
Example 1:
Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]
Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
"""
from typing import List
from heapq import heapify, heappush, heappop
class KthLargest:
    # maintain min heap, we only focus on the top k elements (without actually sorting them)
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = []
        heapify(self.nums)
        for i in nums:
            if len(self.nums) < k: heappush(self.nums, i)
            elif i > self.nums[0]:
                heappop(self.nums)
                heappush(self.nums, i)

    def add(self, val: int) -> int:
        if self.k > len(self.nums): heappush(self.nums, val)
        elif val > self.nums[0]:
            heappop(self.nums)
            heappush(self.nums, val)
        return self.nums[0]