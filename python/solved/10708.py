N = int(input())
M = int(input())
targets = list(map(int, input().split()))
commits = [list(map(int, input().split())) for __ in range(M)]

scores = [0] * N

for inx, target in enumerate(targets):
    commit = commits[inx]
    curr_score = 0
    for jnx in range(N):
        if commit[jnx] == target:
            scores[jnx] += 1
            curr_score += 1
    scores[target - 1] += (N - curr_score)

for score in scores:
    print(score)