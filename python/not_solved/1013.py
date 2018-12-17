import re
pattern = re.compile('(10{2,}1+|01)+')

T = int(input())

for inx in range(T):
    input_str = input()
    search_result = pattern.search(input_str)

    if search_result.start() == 0 and search_result.end() == len(input_str):
        print('YES')
    else:
        print('NO')