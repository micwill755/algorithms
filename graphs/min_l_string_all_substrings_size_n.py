def solution(grid, word):
    res = []
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            s = set(word)
            
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, 1), (-1,-1)]
            for x, y in directions:
                if not len(s):
                    res.append((i, j))
                    break
                new_i = i + x
                new_j = j + y  
                while 0 <= new_i < len(grid) and 0 <= new_j < len(grid):
                    if grid[new_i][new_j] in s:
                        s.remove(grid[new_i][new_j])
    return res

grid = [['a','b','a','b'],['a','b','e','b'],['e','b','e','b']]
word = 'abe'
print(solution(grid, word))