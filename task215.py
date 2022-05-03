
class Solution:
    def partition(self, nums, l, r):
        i, j, pivot = l, r, nums[l]
        while i < j:
            while i < j and nums[j] >= pivot:
                j -= 1
            nums[i] = nums[j]
            while i < j and nums[i] <= pivot:
                i += 1
            nums[j] = nums[i]
        nums[i] = pivot
        return i
    def topk_split(self, nums, k, i, j):
        if i < j:
            mid = self.partition(nums, i, j)
            if mid == k:
                return
            elif mid < k:
                self.topk_split(nums, k, mid + 1, j)
            else:
                self.topk_split(nums, k, i, mid - 1)

    def findKthLargest(self, nums: list[int], k: int) -> int:
        self.topk_split(nums, len(nums) - k, 0, len(nums) - 1)
        return nums[-k]

a = [3,2,1,5,6,4]
s = Solution()
s.findKthLargest(a, 2)
print(a)