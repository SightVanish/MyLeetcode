from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            j = len(numbers)-1
            while i < j:
                if numbers[i]+numbers[j] < target: i += 1
                elif numbers[i]+numbers[j] > target: j -= 1
                else: return [i+1, j+1]
        