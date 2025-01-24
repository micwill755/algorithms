# Python Program to implement
# the above approach
from collections import deque
from typing import Deque, List, Set
 
# Function to print all possible shortest
# sequences starting from start to target.
def displaypath(res: List[List[str]]):
    for i in res:
        print("[ ", end="")
        for j in i:
            print(j, end=", ")
        print("]")
 
# Find words differing by a single
# character with word
def addWord(word: str, Dict: Set):
    res: List[str] = []
    wrd = list(word)
     
    # Find next word in dict by changing
    # each element from 'a' to 'z'
    for i in range(len(wrd)):
        s = wrd[i]
        c = 'a'
        while c <= 'z':
            wrd[i] = c
            if ''.join(wrd) in Dict:
                res.append(''.join(wrd))
            c = chr(ord(c) + 1)
        wrd[i] = s
    return res
 
# Function to get all the shortest possible
# sequences starting from 'start' to 'target'
def findLadders(Dictt: List[str], beginWord: str, endWord: str):
 
    # Store all the shortest path.
    res: List[List[str]] = []
 
    # Store visited words in list
    visit = set()
 
    # Queue used to find the shortest path
    q: Deque[List[str]] = deque()
 
    # Stores the distinct words from given list
    Dict = set()
    for i in Dictt:
        Dict.add(i)
    q.append([beginWord])
 
    # Stores whether the shortest
    # path is found or not
    flag = False
    while q:
        size = len(q)
        for i in range(size):
 
            # Explore the next level
            cur = q[0]
            q.popleft()
            newadd = []
 
            # Find words differing by a
            # single character
            newadd = addWord(cur[-1], Dict)
 
            # Add words to the path.
            for j in range(len(newadd)):
                newline = cur.copy()
                newline.append(newadd[j])
 
                # Found the target
                if (newadd[j] == endWord):
                    flag = True
                    res.append(newline)
 
                visit.add(newadd[j])
                q.append(newline)
 
        # If already reached target
        if (flag):
            break
 
        # Erase all visited words.
        for it in visit:
            Dict.remove(it)
        visit.clear()
    return res
 
# Driver Code
if __name__ == "__main__":
 
    string = ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]
    beginWord = "red"
    endWord = "tax"
 
    res = findLadders(string, beginWord, endWord)
 
    displaypath(res)
 
# This code is contributed by sanjeev2552