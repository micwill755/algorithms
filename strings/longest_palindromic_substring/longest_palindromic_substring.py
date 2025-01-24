'''
Longest Palindromic Substring

Given a string s, return the longest
palindromic
substring
in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

'''

''' brute force '''
def check_palindromic_string(str):
    for i in range(len(str)//2):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

# time complexity is O(n^3)
# auxiliary space O(1)
# space complexity O(n + 1)
def get_longest_palindromic_string(str):
    longest = ""
    for i in range(len(str)):
        for j in range(i, len(str)):
            if check_palindromic_string(str[i:j+1]):
                if len(str[i:j+1]) > longest:
                    longest = str[i:j+1]          

    return longest

''' brute force '''

''' optimate option 1 - not using DP '''

# time complexity is O(n^3)
# auxiliary space O(1)
# space complexity O(n + 1)
def longestPalindrome(str):
    res = ""
    resLen = 0
    for i in range(len(str)):
        # odd length
        l, r = i, i
        while l >= 0 and r < len(str) and str[l] == str[r]:
            if (r - l + 1) > resLen:
                res = str[l:r + 1]
                resLen = r - l + 1
            l -= 1
            r += 1
        # even length
        l, r = i, i + 1
        while l >= 0 and r < len(str) and str[l] == str[r]:
            if (r - l + 1) > resLen:
                res = str[l:r + 1]
                resLen = r - l + 1
            l -= 1
            r += 1
    return res

''' optimate option 2 - using DP '''

# Function to find the longest palindrome substring
def longest_pal_substr(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]

    # All substrings of length 1 are palindromes
    max_len = 1
    start = 0

    for i in range(n):
        dp[i][i] = True

    # Check for sub-string of length 2
    # checks for any even palindromes of len 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2

    # Check for lengths greater than 2
    # k is the length so from length of 3 to size of string
    for k in range(3, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1
            if dp[i + 1][j - 1] and s[i] == s[j]:
                dp[i][j] = True

                if k > max_len:
                    start = i
                    max_len = k

    return s[start:start + max_len]

''' optimate option 2 - using DP '''

if __name__ == "__main__":
    print(longest_pal_substr("geeks"))
    #print(longest_pal_substr("babab"))