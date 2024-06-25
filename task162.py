class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        if len(nums) <= 1: return 0
        l, r = 0, len(nums) - 1
        while l < r:
            if r == l + 1: return r if nums[r] > nums[l] else l
            mid = (l + r) // 2
            if nums[mid + 1] > nums[mid]: l = mid + 1
            else: r = mid
        return l # l == r

# in this question, max number must be the peak->our task is to find the max
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        if len(nums) == 1: return 0
        def find(i, j):
            if j == i: return i
            if j - i == 1: return i if nums[i] > nums[j] else j
            mid = (i + j) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]: return mid
            if nums[mid - 1] > nums[mid + 1]: return find(i, mid - 1)
            else: return find(mid + 1, j)
        return find(0, len(nums) - 1)

s = Solution()
print(s.findPeakElement([3,1,2]))
