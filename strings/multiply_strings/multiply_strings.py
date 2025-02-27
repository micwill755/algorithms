'''

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"

'''

def multiply(num1, num2):
    if num1 == "0" or num2 == "0":
        return "0"

    pow_i = 0
    product = 0

    n1_rev = num1[::-1] 
    n2_rev = num2[::-1] 

    for i in range(len(n2_rev)):
        carry = 0
        pow = -1
        total = 0

        for j in range(len(n1_rev)):
            n1 = ord(n2_rev[i]) - 48
            n2 = ord(n1_rev[j]) - 48
            multiple = (n1 * n2) + carry
            carry = multiple // 10
            pow += 1
            z = (10 ** pow)
            total += (multiple % 10) * z
        
        product += total * (10 ** pow_i)
        pow_i += 1
    return str(product)

# Example 1
num1 = "2"
num2 = "6"
print(multiply(num1, num2))
# Output: "213739916"

# Example 2
num1 = "123"
num2 = "456"
print(multiply(num1, num2))