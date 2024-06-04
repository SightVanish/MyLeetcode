from typing import List
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        n = len(beginWord)
        visited, queue = set(), deque()
        queue.append([beginWord, 1])
        while queue:
            curr, step = queue.popleft()
            if curr == endWord: return step
            visited.add(curr)
            for i in range(n):
                for a in alphabet:
                    if curr[i] != a:
                        new = curr[:i] + a + curr[i+1:]
                        if new in wordList and new not in visited: queue.append((new, step+1))
        return 0
            



