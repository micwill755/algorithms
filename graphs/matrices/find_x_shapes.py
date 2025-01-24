'''
Find the number of ‘X’ total shapes
Last Updated : 21 Feb, 2023
Given a grid of size N * M consisting of O’s and X’s. The task is to find the number of ‘X’ total shapes.

Note: ‘X’ shape consists of one or more adjacents X’s (diagonals not included).

Examples:


Input: grid = {{X, O, X}, {O, X, O}, {X, X, X}}
Output: 3
Explanation: The grid is:
X O X   |   X O X   |  X O X 
O X O  |   O X O   |  O X O
X X X   |   X X X    |  X X X
So, X with bold color are adjacent to each other vertically for horizontally (diagonals not included). So, there are 3 different groups in the given grid.


Input: grid = {{X, X}, {X, X}}
Output: 1
Explanation: The grid is: 
X X
X X
So, X with bold color are adjacent to each other vertically for horizontally (diagonals not included). So, there is only 1 group in the given grid.
 
'''

def dfs(m, x, y):
    if x < 0 or y < 0 or x > len(m)-1 or y > len(m[0])-1:
        return
    
    if m[x][y] == "X":
        m[x][y] = "0"
        dfs(m, x+1, y)
        dfs(m, x-1, y)
        dfs(m, x, y+1)
        dfs(m, x, y-1)

def count_shapes(matrix):
    count = 0
    width = len(matrix[0])
    height = len(matrix)

    for row in range(width):
        for col in range(height):
            if matrix[col][row] == "X":
                count += 1
                dfs(matrix, col, row)
    return count

if __name__ == "__main__":
    # example 1
    '''matrix = [
        ["X", "O", "X"], 
        ["O", "X", "O"],
        ["X", "X", "X"]
    ]'''

    # example 2
    matrix = [
        ["X", "X"], 
        ["X", "X"]
    ]

    print(count_shapes(matrix))