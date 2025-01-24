'''
Consider a situation with a number of persons and the following tasks to be performed on them:

Add a new friendship relation, i.e. a person x becomes the friend of another person y i.e adding new element to a set.
Find whether individual x is a friend of individual y (direct or indirect friend)
Examples: 


We are given 10 individuals say, a, b, c, d, e, f, g, h, i, j


Following are relationships to be added:
a <-> b  
b <-> d
c <-> f
c <-> i
j <-> e
g <-> j


Given queries like whether a is a friend of d or not. We basically need to create following 4 groups and maintain a quickly accessible connection among group items:
G1 = {a, b, d}
G2 = {c, f, i}
G3 = {e, g, j}
G4 = {h}

Partitioning the individuals into different sets according to the groups in which they fall. This method is known as a Disjoint set Union which maintains a collection of Disjoint sets and each set is represented by one of its members.

'''
 
class DisjointSet: 
    def __init__(self, size): 
        self.parent = [i for i in range(size)] 
        self.rank = [0 for _ in range(size)]
        '''print(self.parent)
        print(self.rank)'''
  
    # Function to find the representative (or the root node) of a set 
    def find(self, i): 
        # If i is not the representative of its set, recursively find the representative 
        if self.parent[i] != i: 
            self.parent[i] = self.find(self.parent[i])  # Path compression 
        return self.parent[i] 
  
    # Unites the set that includes i and the set that includes j by rank 
    def union_by_rank(self, i, j): 
        # Find the representatives (or the root nodes) for the set that includes i and j 
        irep = self.find(i) 
        jrep = self.find(j)
  
        # Elements are in the same set, no need to unite anything 
        if irep == jrep: 
            return
  
        # Get the rank of i's tree 
        irank = self.rank[irep] 
  
        # Get the rank of j's tree 
        jrank = self.rank[jrep] 

        # If i's rank is less than j's rank 
        if irank < jrank: 
            # Move i under j 
            self.parent[irep] = jrep 
        # Else if j's rank is less than i's rank 
        elif jrank < irank: 
            # Move j under i 
            self.parent[jrep] = irep 
        # Else if their ranks are the same 
        else: 
            # Move i under j (doesn't matter which one goes where) 
            self.parent[irep] = jrep 
            # Increment the result tree's rank by 1 
            self.rank[jrep] += 1
        print(self.parent)
        print(self.rank)

# Example usage 
size = 5
ds = DisjointSet(size) 

# Perform some union operations 
ds.union_by_rank(0, 1) 
ds.union_by_rank(2, 3) 
#ds.union_by_rank(1, 3) 

# Find the representative of each element 
for i in range(size): 
    print(f"Element {i} belongs to the set with representative {ds.find(i)}") 

