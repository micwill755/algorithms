'''

7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21

'''

def reverse(x):
    s = str(x)
    o = ''
    for i in range (len(s) - 1, -1, -1):
        if s[i] == '-':
            o = '-' + o
        else:
            o += s[i]
    if int(o) > 2**31 - 1 or int(o) < -2**31:
        return 0
    return int(o)

'''def reverse(x):
    s = str(x)
    o = ''
    for i in range (len(s) - 1, -1, -1):
        if s[i] == '-':
            o = '-' + o
        else:
            o += s[i]
    return int(o)'''

if __name__ == '__main__':
    print(reverse(120))