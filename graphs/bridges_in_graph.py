'''
Bridges in a graph
Given an undirected Graph, The task is to find the Bridges in this Graph. 

An edge in an undirected connected graph is a bridge if removing it disconnects the graph. For a disconnected undirected graph, the definition is similar, a bridge is an edge removal that increases the number of disconnected components. 
Like Articulation Points, bridges represent vulnerabilities in a connected network and are useful for designing reliable networks.

'''
 
def dfs_rec(adj, visited, bridges, s):
    # Mark the current vertex as visited
    visited[s] = True

    leaves = 0
    children = len(adj[s])
    
    # Recursively visit all adjacent vertices
    # that are not visited yet
    for i in adj[s]:
        if len(adj[i]) == 1:
            leaves += 1
            
        if not visited[i]:
            dfs_rec(adj, visited, bridges, i)

        print(s, children, leaves, i)
        if len(adj[i]) == 1:
            bridges.append([s, i])
        if children == 2 and leaves == 1:
            bridges.append([s, i])
            
            
def dfs(adj, s):
    visited = [False] * len(adj)
    bridges = []

    # Call the recursive DFS function
    dfs_rec(adj, visited, bridges, s)
    #print(is_leaf)
    #print(adj)
    print(bridges)

def add_edge(adj, s, t):
    # Add edge from vertex s to t
    adj[s].append(t)
    # Due to undirected Graph
    adj[t].append(s)
    
if __name__ == "__main__":
    # Define the edges of the graph
    # example 1
    edges = [[1, 0], [1, 2], [2, 0], [0, 3], [3, 4]]
    v = 5
    s = 1
    # example 2
    '''edges = [[0, 2], [0, 1], [2, 1], [1, 6], [1, 4], [1, 3], [3, 5], [4, 5]]
    v = 7
    s = 0'''
    
    # example 3
    '''edges = [[0, 1], [1, 2], [2, 3]]
    v = 4
    s = 0'''
    # Create an adjacency list for the graph
    adj = [[] for _ in range(v)]
    # Populate the adjacency list with edges
    for e in edges:
        add_edge(adj, e[0], e[1])

    print(adj)
    dfs(adj, s)