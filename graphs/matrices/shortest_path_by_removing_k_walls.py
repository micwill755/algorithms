'''
Shortest path by removing K walls
Last Updated : 23 Feb, 2023
Given a 2D binary matrix of size N * M, where 0 represents an empty space while 1 represents a wall you cannot walk through. You are also given an integer K. You can walk up, down, left, or right. Given that you can remove up to K walls, return the minimum number of steps to walk from the top left corner (0, 0) to the bottom right corner (N-1, M-1). 

Note: If there is no way to walk from the top left corner to the bottom right corner, return -1.

Examples:


Input: N = 3, M = 3, K = 1
mat = {{0, 0, 0}, {0, 0, 1}, {0, 1, 0}}
Output: 4
Explanation: We can remove any one of the walls and reach the bottom in 4 moves.

The below image gives the paths through which we can go from the source to the destination

Image showing most of the paths from the source to the destination

If we carefully observe the paths shown above then, we will see that in these paths we have one cell that contains 1 and since we have k=1 hence we can traverse this cell also, and hence it gives the minimum steps.

Input: N = 2, M = 2, K = 0
mat[] = {{0, 1}, {1, 0}}
Output: -1
Explanation: There’s no way of reaching the bottom corner without removing any walls.

'''

# DFS will not work because we have to revisit nodes through multiple paths
# DFS will find a path but not necessarily the shortest 
def dfs_find_path(matrix, n, m, k, s, visited, p, found):
    # if we found bottom right corner
    if s[0] == (m - 1) and s[1] == (n - 1):
        found[0] = True
        print ('Path found', len(p), p)
    
    # Mark the current element as visited
    visited[s[0]][s[1]] = True

    # get neighbours
    neighbours = []
    # check left
    if s[0] > 0:
        neighbours.append([s[0]-1, s[1]])
    # check right
    if s[0] < (m-1):
        neighbours.append([s[0]+1, s[1]])
    # check up
    if s[1] > 0:
        neighbours.append([s[0], s[1]-1])
    # check down
    if s[1] < n-1:
        neighbours.append([s[0], s[1]+1]) 

    for neighbour in neighbours:
        # if the neighbour is not visited
        if not visited[neighbour[0]][neighbour[1]]:
            # if we have a '0' 
            if matrix[neighbour[0]][neighbour[1]] == 0:
                dfs_find_path(matrix, n, m, k, neighbour, visited, p + [neighbour], found)
            # if we have a '1' and more k to remove wall
            if matrix[neighbour[0]][neighbour[1]] == 1 and k[0] > 0:
                dfs_find_path(matrix, n, m, [k[0] - 1], neighbour, visited, p + [neighbour], found)
      
if __name__ == "__main__":
    # example 1
    matrix = [
        [0, 0, 0], 
        [0, 1, 0],
        [1, 1, 0]
    ]

    k = [1]

    # example 2
    '''matrix = [
        [0, 1], 
        [1, 0]]

    k = [0]'''
    # start top left
    source = [0, 0]

    path = [source]
    dfs_find_path(matrix, len(matrix[0]), len(matrix), k, source, [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))], path, [False])
    #print(shortestPath(matrix, k[0]))
