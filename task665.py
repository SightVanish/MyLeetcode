# simple solution
def CheckNonDecreasing(nums) -> bool:
    if len(nums) == 0:
        return True
    v = nums[0]
    for i in nums:
        if i >= v:
            v = i
        else:
            return False
    return True

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            mask = nums[:i] + nums[i+1:]
            if CheckNonDecreasing(mask):
                return True
        return False


# advanced solution
# consider nums[i], nums[i-1] and nums[i-2]
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if nums is None or len(nums) == 1:
            return True
        count = 0 # how many times we have modified
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                count += 1
                if i==1:
                    nums[i-1] = nums[i]
                else:
                    if nums[i-2] <= nums[i]:
                        nums[i-1] = nums[i]
                    else:
                        nums[i] = nums[i-1]
            if count > 1:
                return False
        return count <= 1
                        