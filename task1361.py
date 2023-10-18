"""
You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.
If node i has no left child then leftChild[i] will equal -1, similarly for the right child.
Note that the nodes have no values and that we only use the node numbers in this problem.
"""




from typing import List
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parents = [-1] * n
        # find the parent of each node
        for i, j in enumerate(leftChild):
            if j != -1:
                if parents[j] == -1: parents[j] = i
                else: return False # each node has at most one parent
        for i, j in enumerate(rightChild):
            if j != -1:
                if parents[j] == -1: parents[j] = i
                else: return False
        if parents.count(-1) == 1: # there is one node without parent
            root = parents.index(-1)
            # all nodes must be associated with parent
            found = [root]
            next = [leftChild[root], rightChild[root]]
            while next:
                if next[0] not in found and next[0] != -1:
                    found.append(next[0])
                    next.append(leftChild[next[0]])
                    next.append(rightChild[next[0]])
                next = next[1:]
            return len(found) == n
        return False


s = Solution()
print(s.validateBinaryTreeNodes(5, leftChild = [1,3,-1,-1,-1], rightChild = [-1,2,4,-1,-1]))