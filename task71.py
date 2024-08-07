"""
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.
In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.
The canonical path should have the following format:
The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
Return the simplified canonical path.
Example 1:
Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        path.replace('//', '')
        realpath = []
        path = path.split('/')
        for p in path:
            if p == '' or p == '.':
                continue
            if p == '..':
                if realpath:
                    realpath.pop()
            else:
                realpath.append(p)
        return '/' + '/'.join(realpath)

class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []
        for i in path:
            if i == '..': 
                if len(stack) > 0: stack.pop()
            elif i not in ['', '.']: stack.append(i)
        return '/' + '/'.join(stack)

s = Solution()
print(s.simplifyPath('/home//foo/'))

