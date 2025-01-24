
'''

given n, how many partition can n be broken into using parts up to m

'''

def count_partitions(n, m):
    if n == 0:
        return 1
    elif n < 0 or m == 0:
        return 0
    else:
        return count_partitions(n - m, m) + count_partitions(n, m - 1)
    
if __name__ == '__main__':
    print(count_partitions(5, 2))