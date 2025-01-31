'''

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"

'''

def zigzag(s, numRows):
    if numRows == 1:
        return s
    rows = [''] * numRows
    row = 0
    step = 1
    
    for c in s:
        rows[row] += c
        if row == 0:
            step = 1
        elif row == numRows - 1:
            step = -1
        row += step

    return ''.join(rows)

'''def zigzag(str, numRows):
    matrix = [[''] * len(str) for _ in range(numRows)]
    row, col = 0, 0
    reversing = False

    for char in str:
        matrix[row][col] = char
        if reversing:
            row -= 1
            col += 1
            if row == 0:
                reversing = False
        else:
            row += 1
            if row == numRows:
                reversing = True
                row -= 2
                col += 1

    output = ''      
    for i in range(numRows):
        for j in range(len(str)):
            if matrix[i][j] != '':
                output += matrix[i][j]

    return output'''

if __name__ == '__main__':
    print(zigzag("PAYPALSHIRING", 3))