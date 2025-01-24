from collections import defaultdict
'''
A tree rooted at node 0 is given as follows:

    The number of nodes is nodes;
    The value of the ith node is value[i];
    The parent of the ith node is parent[i].

Remove every subtree whose sum of values of nodes is zero.

Return the number of the remaining nodes in the tree.

Example 1

Input: nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-1]
Output: 2

Example 2:

Input: nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-2]
Output: 6

'''
 
def dfs(i, g, value):
    # sum starts with parent node val
    s, m = value[i], 1
    # for all parents children 
    for j in g[i]:
        t, n = dfs(j, g, value)
        s += t
        m += n
    if s == 0:
        m = 0
    return (s, m)

def delete_tree_nodes(parent, value):
    nodes = len(parent)
    g = defaultdict(list)
    # we start at 1 because parent of tree is always represented as -1
    for i in range(1, nodes):
        print(i, parent[i])
        g[parent[i]].append(i)
    print(g)
    return dfs(0, g, value)

if __name__ == "__main__":
    parent = [-1, 0, 0, 1, 2, 2, 2]
    value = [1, -2, 4, 0, -2, -1, -1]

    print(delete_tree_nodes(parent, value))