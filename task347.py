from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for i in nums:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1
        max_frequence = max(frequency.values())
        bucket = [[] for i in range(max_frequence + 1)]
        for key in frequency:
            bucket[frequency[key]].append(key)
        ans = []
        j = max_frequence

        # print(bucket)
        while k > 0:
            while len(bucket[j]) == 0:
                j -= 1
            if len(bucket[j]) > k:
                ans += (bucket[j][:k])
            ans += (bucket[j])
            k -= len(bucket[j])
            j -= 1

        return ans


s = Solution()
print(s.topKFrequent([1,2], 2))
