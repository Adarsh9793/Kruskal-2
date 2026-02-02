

def findparent(parent, a):
    if parent[a] == a:
        return a
    parent[a] = findparent(parent, parent[a])  # Path compression
    return parent[a]

def union(rank, parent, a, b):
    parentA = findparent(parent, a)
    parentB = findparent(parent, b)

    if parentA == parentB:
        return

    # Union by rank
    if rank[parentA] > rank[parentB]:
        parent[parentB] = parentA
    elif rank[parentA] < rank[parentB]:
        parent[parentA] = parentB
    else:
        parent[parentB] = parentA
        rank[parentA] += 1


Parent = []
rank = []

adjmatrix = [[0,1,2,0],[1,0,3,1],[2,3,0,5],[0,1,5,0]]

v = len(adjmatrix)

for i in range(v):
    Parent.append(i)
    rank.append(0)

edges = []

# Build edge list
for i in range(v):
    for j in range(v):
        if adjmatrix[i][j] != 0 and i < j:
            edges.append((adjmatrix[i][j], i, j))  # (weight, node1, node2)

# Sort edges by weight
edges = sorted(edges, key=lambda item: item[0])

ans = 0
ansEdges = []

# Kruskal’s Algorithm
for w, u, v in edges:
    parentU = findparent(Parent, u)
    parentV = findparent(Parent, v)

    if parentU == parentV:
        continue

    ans += w
    ansEdges.append((u, v, w))
    union(rank, Parent, u, v)


print("Minimum Cost Spanning Tree:", ans)
for U, V, W in ansEdges:
    print(U," " , V," " , W , "\n")
print("Edges in MST:", ansEdges)
print("Parents Array:", Parent)      

