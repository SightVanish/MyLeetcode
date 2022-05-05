class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            return 0

        l, r = 0, len(nums) - 1
        while l < r:
            if r == l + 1:
                return r if nums[r] > nums[l] else l
            mid = (l + r) // 2
            if nums[mid + 1] > nums[mid]:
                l = mid + 1
            else:
                r = mid
        return l # l == r


s = Solution()
print(s.findPeakElement([3,1,2]))
