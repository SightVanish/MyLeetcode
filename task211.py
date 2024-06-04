from collections import deque
class WordDictionary:

    def __init__(self):
        self.trie = {} 

    def addWord(self, word: str) -> None:
        curr = self.trie
        for l in word:
            if l not in curr: curr[l] = {}
            curr = curr[l]
        if 'end' not in curr: curr['end'] = {}

    def search(self, word: str) -> bool:
        def subSearch(word, wordDict):
            if word == '':
                if 'end' in wordDict: return True
                else: return False
            if word[0] == '.':
                for key in wordDict.keys():
                    if key != 'end' and subSearch(word[1:], wordDict[key]): return True
            else:
                if word[0] in wordDict and subSearch(word[1:], wordDict[word[0]]): return True
            return False
        return subSearch(word, self.trie)

    
w = WordDictionary()
w.addWord('at')
w.addWord('and')
w.addWord('an')
w.addWord('add')
print(w.search('a'))
# print(w.search('.at'))
