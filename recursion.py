
'''

Longest Common Subsequence (LCS)
Last Updated : 23 Aug, 2024
Given two strings, S1 and S2, the task is to find the length of the Longest Common Subsequence. If there is no common subsequence, return 0. A subsequence is a string generated from the original string by deleting 0 or more characters and without changing the relative order of the remaining characters. For example , subsequences of “ABC” are “”, “A”, “B”, “C”, “AB”, “AC”, “BC” and “ABC”. In general a string of length n has 2n subsequences.

LCS problem has great applications like diff utility (find the difference between two files) that we use in our day to day software development.

Examples:

Input: S1 = “ABC”, S2 = “ACD”
Output: 2
Explanation: The longest subsequence which is present in both strings is “AC”.

Input: S1 = “AGGTAB”, S2 = “GXTXAYB”
Output: 4
Explanation: The longest common subsequence is “GTAB”.

Input: S1 = “ABC”, S2 = “CBA”
Output: 1
Explanation: There are three common subsequences of length 1, “A”, “B” and “C” and no common subsequence of length more than 1.

'''

def sum_non_negative(n):
    if n == 1:
        return 1
    return n + sum_non_negative(n-1)


def grid_paths(n, m):
    if n == 1 or m == 1:
        return 1
    return grid_paths(n-1, m) + grid_paths(n, m-1)

if __name__ == '__main__':
    print(grid_paths(3, 3))