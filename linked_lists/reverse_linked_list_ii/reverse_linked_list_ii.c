/*

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


*/

// C++ implementation of optimized Approach 1
#include <bits/stdc++.h>
using namespace std;
 
// function to simplify a Unix - styled
// absolute path
string simplify(string path)
{
    // using vector in place of stack
    vector<string> v;
    int n = path.length();
    string ans;
    for (int i = 0; i < n; i++) {
        string dir = "";
        // forming the current directory.
        while (i < n && path[i] != '/') {
            dir += path[i];
            i++;
        }
 
        // if ".." , we pop.
        if (dir == "..") {
            if (!v.empty())
                v.pop_back();
        }
        else if (dir == "." || dir == "") {
            // do nothing (added for better understanding.)
        }
        else {
            // push the current directory into the vector.
            v.push_back(dir);
        }
    }
 
    // forming the ans
    for (auto i : v) {
        ans += "/" + i;
    }
 
    // vector is empty
    if (ans == "")
        return "/";
 
    return ans;
}
 
// Driver Code
int main()
{
    // absolute path which we have to simplify.
    string str("/a/./b/../../c/");
    string res = simplify(str);
    cout << res;
    return 0;
}
 
// This code is contributed by yashbeersingh42