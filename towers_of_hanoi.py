# Recursive Python function to solve tower of hanoi


def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)

# using no aux input
def TowerOfHanoiNoAux(n, start, end):
    if n == 0:
        return
    other = 6 - (start + end)
    TowerOfHanoiNoAux (n-1, start, other)
    print("Move disk", n, "from rod", start, "to rod", end)
    TowerOfHanoiNoAux (n-1, other, end)

# Driver code
N = 3

# A, C, B are the name of rods
#TowerOfHanoi(N, 'A', 'C', 'B')
TowerOfHanoiNoAux(N, 1, 3)

# Contributed By Harshit Agrawal