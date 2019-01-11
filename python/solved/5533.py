N= int(input())
original_commits = [list(map(int, input().split())) for __ in range(N)]

def rotate(original):
    return list(map(lambda x: list(x), zip(*reversed(original))))

commits = rotate(original_commits)
scores = [0] * N

for row in commits:
    for inx in range(len(row) - 1, -1, -1):
        curr_commit = row[inx]
        if row.count(curr_commit) == 1:
            scores[N - 1 - inx] += curr_commit

print(*scores)
