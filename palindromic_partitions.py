# Recursive Python function to solve tower of hanoi

def checkPalindrome(s):
    print (s)
    mid = len (s) // 2
    count = 0
    for i in range (mid):
        if (s[i] != s[len (s) - i - 1]):
            return False
        else:
            count += 1
    if (count == mid):
        return True

# geek for geeks
'''def partition(res, s, ind, curr):
    if ind == len(s):
        res.append(list(curr))
        return curr

    temp = ""
    for i in range(ind, len(s)):
        temp += s[i]
        if checkPalindrome(temp):
            curr.append(temp)
            partition(res, s, i + 1, curr)
            curr.pop()
res = []
s = "geeks"
ind = 0
curr = []
partition(res, s, ind, curr)

for iter in res:
    print(iter)'''

def palindromic_partitions (s, arr):
    if len(s) < 1:
        print (arr)
    else:
        temp = ""
        for i in range(len(s)):
            temp += s[i]
            if checkPalindrome(temp):
                arr.append(temp)
                palindromic_partitions(s[1:], arr)
                arr.pop()

arr = []
palindromic_partitions("geeks", arr)