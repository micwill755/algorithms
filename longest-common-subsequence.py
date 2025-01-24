
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

inputs = [
    ['ABC', 'ACD'],
    ['AGGTAB', 'GXTXAYB'],
    ['ABC', 'CBA']
]

def check_small_string(s1, s2):
    if len(s1) < len(s2):
        return s1, s2
    else:
        return s2, s1

def check_for_char_match(small, char, j, m):
    if j == m:
        return [0, 0]
    else:
        if small[j] == char:
            return [1, j]
        return check_for_char_match(small, char, j+1, m)

def longest_common_subsequence(small, large, i, n, mx, lf):
    if n == i:
        return 0
    else:
        res = check_for_char_match (small, large[i], lf, len(small))
        # set last found index to res[1] for next iteration of small word
        if res[1] != 0:
            lf = res[1]
        mx += res[0]
        return max(mx, longest_common_subsequence(small, large, i+1, n, mx, lf))

def run_examples():
    count = 1
    for arr in inputs:
        small, large = check_small_string(arr[0], arr[1])
        print ('example {} - LIS {}'.format(count, longest_common_subsequence(small, large, 0, len(large), 0, 0)))
        count += 1

if __name__ == '__main__':
    run_examples()