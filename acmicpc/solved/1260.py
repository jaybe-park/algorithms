N, M, V = map(int, input().split())
tree = dict()
for __ in range(M):
    parent, child = map(int, input().split())
    
    if parent in tree.keys():
        tree[parent].append(child)
    else:
        tree[parent] = [child]

    if child in tree.keys():
        tree[child].append(parent)
    else:
        tree[child] = [parent]


# sort
for key in tree.keys():
    tree[key].sort()

# dfs
dfs_check = [False] * (N + 1)
def dfs(target_node):
    if dfs_check[target_node]:
        return
    dfs_result.append(target_node)
    dfs_check[target_node] = True
    if target_node in tree.keys():
        sorted_children = tree[target_node]
        for child in sorted_children:
            dfs(child)

dfs_result = []
dfs(V)
print(' '.join(map(str, dfs_result)))

# bfs
queue = []
bfs_check = [False] * (N + 1)
def bfs():
    target_node = queue.pop(0)

    bfs_result.append(target_node)
    bfs_check[target_node] = True

    if target_node in tree.keys():
        sorted_children = tree[target_node]
        for child in sorted_children:
            if (not bfs_check[child]) and (not child in queue):
                queue.append(child)

bfs_result = []
queue.append(V)
bfs_check[V] = True

while len(queue) != 0:
    bfs()
print(' '.join(map(str, bfs_result)))