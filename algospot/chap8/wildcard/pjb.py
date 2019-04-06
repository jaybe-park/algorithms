import re
import sys

C = int(sys.stdin.readline())
for __ in range(C):
    pattern = sys.stdin.readline().strip()
    pattern = '^' + pattern.replace('?', '.').replace('*', '[a-zA-z0-9]*') + '$'

    compiler = re.compile(pattern)

    result = []

    N = int(sys.stdin.readline())
    for ___ in range(N):
        target = sys.stdin.readline().strip()
        if compiler.match(target) != None:
            result.append(target)

    if len(result) > 0:
        result.sort()
        for r in result:
            print(r)
