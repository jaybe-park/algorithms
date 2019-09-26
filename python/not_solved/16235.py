# pypy로는 통과
# Python3 불가능


import sys.stdin
input = stdin.readline

N, M, K = map(int, input().split())
nutrients = [[5] * N for __ in range(N)]
added_nutrients = []
for __ in range(N):
    added_nutrients.append(list(map(int, input().split())))

ground = []
for __ in range(N):
    ground.append([[] * N for inx in range(N)])

for __ in range(M):
    x, y, year = map(int, input().split())
    ground[x - 1][y - 1].append(year)

def is_in_ground(inx, jnx):
    if inx < 0 or inx >= N or jnx < 0 or jnx >= N:
        return False
    else:
        return True

EIGHT_DIRECTION = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

for ___ in range(K):
    # Spring & Summer
    for inx, row in enumerate(ground):
        for jnx, tree_list in enumerate(row):
            if len(tree_list) != 0:
                next_tree = []
                next_nutrient = 0
                for tree in tree_list:
                    if tree <= nutrients[inx][jnx]:
                        next_tree.append(tree + 1)
                        nutrients[inx][jnx] -= tree
                    else:
                        next_nutrient += int(tree/2)
                    
                ground[inx][jnx] = next_tree
                nutrients[inx][jnx] += next_nutrient

    # Fall & Winter
    for inx, row in enumerate(ground):
        for jnx, tree_list in enumerate(row):
            for tree in tree_list:
                # Winter
                nutrients[inx][jnx] += added_nutrients[inx][jnx]

                # Fall
                if tree % 5 == 0:
                    for direction in EIGHT_DIRECTION:
                        if is_in_ground(inx + direction[0], jnx + direction[1]):
                            ground[inx + direction[0]][jnx + direction[1]].insert(0, 1)

result = 0
for row in ground:
    for tree_list in row:
        result += len(tree_list)

print(result)
