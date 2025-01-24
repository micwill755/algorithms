'''
Find whether there is path between two cells in matrix
Last Updated : 22 Nov, 2023
Given N X N matrix filled with 1, 0, 2, 3. Find whether there is a path possible from source to destination, traversing through blank cells only. You can traverse up, down, right, and left. 

A value of cell 1 means Source.
A value of cell 2 means Destination.
A value of cell 3 means Blank cell.
A value of cell 0 means Blank Wall.
Note: there are an only a single source and single destination(sink). 
https://www.geeksforgeeks.org/find-whether-path-two-cells-matrix/
Examples:  
Input: 
M[3][3] = {{ 0, 3, 2 }, 
{ 3, 3, 0 }, 
{ 1, 3, 0 }}; 
Output : Yes 

Input: 
M[4][4] = {{ 0, 3, 1, 0 }, 
{ 3, 0, 3, 3 }, 
{ 2, 3, 0, 3 }, 
{ 0, 3, 3, 3 }}; 
Output: Yes 
 
'''

def dfs_find_path(m, s, d, visited, p, found):
    # Mark the current element as visited
    visited[s[0]][s[1]] = True

    # if we have reached he destination
    if s == d:
        # add the destination to path
        found[0] = True
        return
    
    # get neighbours
    neighbours = get_neighbours(m, s[0], s[1], visited)

    for n in neighbours:
        # if the neighbour is not visited
        if not visited[n[0]][n[1]] and not found[0]:
            if m[n[0]][n[1]] == 3 or m[n[0]][n[1]] == 2:
                p.append(n)
                dfs_find_path(m, n, d, visited, p, found)

    return found[0]

def get_neighbours(m, x, y, visited):
    neighbours = []
    # check left
    if x > 0 and m[x-1][y] != 0 and not visited[x-1][y]:
        neighbours.append([x-1, y])
    # check right
    if x < len(m)-1 and m[x+1][y] != 0 and not visited[x+1][y]:
        neighbours.append([x+1, y])
    # check up
    if y > 0 and m[x][y-1] != 0 and not visited[x][y-1]:
        neighbours.append([x, y-1])
    # check down
    if y < len(m[0])-1 and m[x][y+1] != 0 and not visited[x][y+1]:
        neighbours.append([x, y+1])
    return neighbours
    
if __name__ == "__main__":
    # example 1
    '''matrix = [
        [0, 3, 2], 
        [3, 3, 0],
        [1, 3, 0]
    ]

    source = [2, 0]
    destination = [0, 2]'''

    # example 2
    matrix = [
        [0, 3, 1, 0], 
        [3, 0, 3, 3],
        [2, 3, 0, 3],
        [0, 3, 3, 3]]
    
    source = [0, 2]
    destination = [2, 0]
    
    visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    path = []
    # add starting
    path.append(source)
    visited[source[0]][source[1]] = True
    has_path = dfs_find_path(matrix, source, destination, visited, path, [False])
    print(has_path, path)