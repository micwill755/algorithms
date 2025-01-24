
'''

Word Break
Given an input string and a dictionary of words, find out if the input string can be segmented into a space-separated sequence of dictionary words. See following examples for more details. 
This is a famous Google interview question, also being asked by many other companies now a days.

Consider the following dictionary
{ i, like, sam, sung, samsung, mobile, ice,
cream, icecream, man, go, mango}
Input: ilike
Output: Yes
The string can be segmented as “i like”.

Input: ilikesamsung
Output: Yes
The string can be segmented as “i like samsung”
or “i like sam sung”.

'''

# Function to check if the given word can be broken
# down into words from the wordList
def wordBreak(wordList, word):
    # If the word is empty, it can be broken down into
    # an empty list of words
    if not word:
        return True
    
    wordLen = len(word)
    # Check if the word can be broken down into
    # words from the wordList
    for i in range(1, wordLen + 1):
        prefix = word[:i]
        print(prefix)
        if prefix in wordList and wordBreak(wordList, word[i:]):
            return True
    
    return False

wordList = ["mobile", "samsung", "sam", "sung", "man",
                "mango", "icecream", "and", "go", "i",
                "like", "ice", "cream"]
    
result = wordBreak(wordList, "ilikesamsung")
