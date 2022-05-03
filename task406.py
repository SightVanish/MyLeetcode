from typing import List
"""
The key point is you have to sort based on -x[0] then x[1]
"""
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        result = []
        people.sort(key=lambda x:(-x[0], x[1]))
        result.append(people[0])
        
        for i in range(1, len(people)):
            count = 0
            j = 0
            while count < people[i][1]:
                if result[j][0] >= people[i][0]:
                    j += 1
                    count += 1
            result.insert(j, people[i])
        return result


s = Solution()
test = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
print(s.reconstructQueue(test))