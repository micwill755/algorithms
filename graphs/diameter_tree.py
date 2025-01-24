'''
Depth First Search or DFS for a Graph
Depth First Traversal (or DFS) for a graph is similar to Depth First Traversal of a tree. Like Trees, we traverse all adjacent one by one, when we traverse an adjacent, we finish traversal of all vertices reachable through the adjacent completely. After we finish one adjacent and its reachable, we go to the next adjacent and finish all reachable through next and continue this way. Similar to tree where we first completely traverse the left subtree and then go to the right subtree. The only catch here is, that, unlike trees, graphs may contain cycles (a node may be visited twice). To avoid processing a node more than once, use a boolean visited array.

'''
 
def dfs_rec(adj, visited, s, edge_count, diametre):
    # Mark the current vertex as visited
    visited[s] = True

    if edge_count > diametre[0]:
        diametre[0] = edge_count

    # Recursively visit all adjacent vertices
    # that are not visited yet
    for i in adj[s]:
        if not visited[i]:
            dfs_rec(adj, visited, i, edge_count + 1, diametre)


def dfs(adj, s, edge_count, diametre):
    visited = [False] * len(adj)
    # Call the recursive DFS function
    dfs_rec(adj, visited, s, edge_count, diametre)

def add_edge(adj, s, t):
    # Add edge from vertex s to t
    adj[s].append(t)
    # Due to undirected Graph
    adj[t].append(s)
    
if __name__ == "__main__":
    edges = [[0,1],[0,2]]

    V = len(edges) + 1
    # Create an adjacency list for the graph
    adj = [[] for _ in range(V)]

    # Populate the adjacency list with edges
    for e in edges:
        add_edge(adj, e[0], e[1])

    source = 0
    print("DFS from source:", source)
    diametre = [0]
    dfs(adj, source, 1, diametre)
    print("Diametre:", diametre[0])