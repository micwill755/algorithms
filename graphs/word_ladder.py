from typing import List, Tuple, Set, Dict, Any, Union
# Python Program to implement
# the above approach
from collections import deque
from typing import Deque, List, Set

def shortest_chain_len(start: str, target: str, D: Set[str]) -> int:
    if start == target:
        return 0

    # Dictionary of intermediate words and
    # the list of original words
    umap: Dict[str, List[str]] = {}

    # Initialize umap with empty lists
    for i in range(len(start)):
        intermediate_word = start[:i] + "*" + start[i+1:]
        umap[intermediate_word] = []

    # Find all the intermediate words for
    # the words in the given Set
    for word in D:
        for i in range(len(word)):
            intermediate_word = word[:i] + "*" + word[i+1:]
            if intermediate_word not in umap:
                umap[intermediate_word] = []
            umap[intermediate_word].append(word)

    # Perform BFS and push (word, distance)
    q = [(start, 1)]
    visited = {start: 1}

    # Traverse until queue is empty
    while q:
        word, dist = q.pop(0)

        # If target word is found
        if word == target:
            return dist

        # Finding intermediate words for
        # the word in front of queue
        for i in range(len(word)):
            intermediate_word = word[:i] + '*' + word[i+1:]
            vect = umap[intermediate_word]
            for k in range(len(vect)):
              
                # If the word is not visited
                if vect[k] not in visited:
                    visited[vect[k]] = 1
                    q.append((vect[k], dist + 1))

    return 0

# Test

# Make dictionary
'''D = {'poon', 'plee', 'same', 'poie', 'plie', 'poin', 'plea'}
start = "toon"
target = "plea"
print(f"Length of shortest chain is: {shortest_chain_len(start, target, D)}")'''

def get_all_shortest_chain(start, target, d):
    #q = []
    #q.append([start])

    # Queue used to find the shortest path
    q: Deque[List[str]] = deque()
    q.append([start])
    result = []
    found_path = False

     # Store visited words in list
    visit = set()

    while(len(q) > 0):
        size = len(q)
        for i in range(size):
            # first pop the queue to get chain
            #cur = q.pop()
            #word = [j for j in cur.pop()]

            cur = q[0]
            q.popleft()
            add_words = []

            word = list(cur[-1])

            for i in range(len(word)):
                orig_char = word[i]
                # loop through alphabet
                for c in range(ord('a'), ord('z')+1):
                    word[i] = chr(c)
                    if "".join(word) in d:
                        add_words.append(''.join(word))
                word[i] = orig_char

            for w in add_words:
                new_line = cur.copy()
                new_line.append("".join(w))

                if "".join(w) == target:
                    found_path = True
                    result.append(new_line)

                visit.add("".join(w))
                q.append(new_line)

        if found_path:
            break
        
        # Erase all visited words.
        for it in visit:
            d.remove(it)
        visit.clear()

    return result

'''def get_shortest_chain(start, target, d):
    queue = []
    result = []
    result.append(start)
    queue.append(start)
    level = 0

    while(len(queue) > 0):
        level += 1
        word = [j for j in queue.pop()]
        for i in range(len(start)):
            orig_char = word[i]
            # loop through alphabet
            for c in range(ord('a'), ord('z')+1):
                word[i] = chr(c)
                # if target found return total levels 
                # to count BFS depth
                if "".join(word) == target:
                    result.append("".join(word))
                    return result
                # if the word is not in dictionary 
                # try next character of alphabet
                if "".join(word) not in d:
                    continue
                # the word is in dict, remove and add to queue
                del d["".join(word)]
                queue.append("".join(word))
                result.append("".join(word))

            # replace changed word character to original
            word[i] = orig_char

    return 0
'''

if __name__ == '__main__':
    # Make dictionary
    d = set()
    d.add("ted")
    d.add("tex")
    d.add("red")
    d.add("tax")
    d.add("tad")
    d.add("den")
    d.add("rex")
    d.add("pee")
    start = "red"
    target = "tax"
    
    print("Length of shortest chain is: ",
    get_all_shortest_chain(start, target, d))

# This code is contributed by mohit kumar 29