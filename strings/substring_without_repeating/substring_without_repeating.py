'''

3. Longest Substring Without Repeating Characters
Medium
Topics
Companies
Hint
Given a string s, find the length of the longest 
substring
 without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

'''

# O(n^2)
# aux space O(3 + len(sub))
# space O(3 + len(sub) + len(text))
def longest_substring_without_repeating(text):
    '''if len(s) == 0:
        return 0
    
    char_set = set()
    max_length = 0
    left = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length'''

  
    if len(text) == 0:
        return 0
    
    s = 0
    sub = ''

    for c in range(1, len(text)):
        temp = c - 1
        while temp >= s:
            if text[c] == text[temp]:
                if len(text[s:c]) > len(sub):
                    sub = text[s:c]
                s = c
                break
            temp -= 1
    
    return sub
    
if __name__ == "__main__":
    text = "abcabcbb"
    print(longest_substring_without_repeating(text))
    text = "bbbbb"
    print(longest_substring_without_repeating(text))
    text = "pwwkew"
    print(longest_substring_without_repeating(text))