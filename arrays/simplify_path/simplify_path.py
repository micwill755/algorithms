'''

You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.

The rules of a Unix-style file system are as follows:

A single period '.' represents the current directory.
A double period '..' represents the previous/parent directory.
Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.
The simplified canonical path should follow these rules:

The path must start with a single slash '/'.
Directories within the path must be separated by exactly one slash '/'.
The path must not end with a slash '/', unless it is the root directory.
The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
Return the simplified canonical path.

'''

# Python3 implementation of optimized Approach 1
 
# function to simplify a Unix - styled
# absolute path
def simplify(path):
    # using vector in place of stack
    stack = []
    cur = ""
    ans = ""
    
    for c in path:
        if c == "/":
            if cur == "..":
                if stack: stack.pop()
            elif cur != "." and cur != "":
                stack.append(cur)
            cur = ""
        else:
            cur += c
    
    # forming the ans
    for i in stack:
        ans += "/" + i
  
    # vector is empty
    if (ans == ""):
        return "/"
    
    return ans
 
# absolute path which we have to simplify.
res = simplify("/.../a/../b/c/../d/./")
print(res)
 
# This code is contributed by rameshtravel07