'''
Depth First Search or DFS for a Graph
Depth First Traversal (or DFS) for a graph is similar to Depth First Traversal of a tree. Like Trees, we traverse all adjacent one by one, when we traverse an adjacent, we finish traversal of all vertices reachable through the adjacent completely. After we finish one adjacent and its reachable, we go to the next adjacent and finish all reachable through next and continue this way. Similar to tree where we first completely traverse the left subtree and then go to the right subtree. The only catch here is, that, unlike trees, graphs may contain cycles (a node may be visited twice). To avoid processing a node more than once, use a boolean visited array.

'''
 
def dfs_adj(adj, visited, s, group):
    # Mark the current vertex as visited
    visited[s] = True

    group.append(s)

    # Recursively visit all adjacent vertices
    # that are not visited yet
    for i in adj[s]:
        if not visited[i]:
            dfs_adj(adj, visited, i, group)


def get_connected(adj):
    visited = [False] * len(adj)
    connected = []

    for i in range(len(adj)):
        group = []
        if not visited[i]:
            dfs_adj(adj, visited, i, group)
        if len(group) > 0:
            connected.append(group)

    return connected

def add_edge(adj, s, t):
    # Add edge from vertex s to t
    adj[s].append(t)
    # Due to undirected Graph
    adj[t].append(s)
    
if __name__ == "__main__":
    V = 5

    # Create an adjacency list for the graph
    adj = [[] for _ in range(V)]

    # Define the edges of the graph
    edges = [[1, 0], [1, 2], [3, 4]]

    # Populate the adjacency list with edges
    for e in edges:
        add_edge(adj, e[0], e[1])

    print(get_connected(adj))