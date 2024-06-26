from typing import List
import heapq
# quick selection -- O(n) and the worst case O(n2)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(i, j):
            pivot = nums[i]
            while i < j:
                while i < j and nums[j] >= pivot: j -= 1
                nums[i] = nums[j]
                while i < j and nums[i] <= pivot: i += 1
                nums[j] = nums[i]
            nums[i] = pivot
            return i
        def topK(i, j):
            if i >= j: return
            pivot = partition(i, j)
            if pivot == len(nums) - k: return 
            elif pivot < len(nums) - k: return topK(pivot + 1, j)
            else: return topK(i, pivot - 1)
        topK(0, len(nums) - 1)
        return nums[-k]

# heap -- O(nlogk)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for i in nums[k:]:
            if i > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, i)
        return heap[0]

a = [3,2,1,5,6,4]
s = Solution()
s.findKthLargest(a, 2)
print(a)