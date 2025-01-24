
'''
Given a decimal number as input, we need to write a program to convert the given decimal number into an equivalent binary number. 

Examples : 

Input : 7                                                         
Output :111

Input :10
Output :1010

'''

def binary(n):
    if n == 1:
        return "1"
    else:
        return binary(n // 2) + str(n % 2)
    
if __name__ == '__main__':
    print(5 // 2)