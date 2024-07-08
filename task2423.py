from collections import defaultdict
class Solution:
    def equalFrequency(self, word: str) -> bool:
        if len(set(word)) == len(word) or len(set(word)) == 1: return True
        frequency = defaultdict(int)
        count_frequency = defaultdict(int)
        for i in word: frequency[i] += 1
        for value in frequency.values(): count_frequency[value] += 1
        max_frequency = max(list(frequency.values()))
        if max_frequency * count_frequency[max_frequency] == len(word) - 1: return True
        if (max_frequency - 1) * count_frequency[max_frequency - 1] + max_frequency - 1 == len(word) - 1: return True
        return False

s = Solution()
print(s.equalFrequency("abcdefghijklmnopqrstuvwxyznabcdefghijklmnopqrstuvwxyz"))
