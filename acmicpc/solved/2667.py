N = int(input())
my_map = []
for __ in range(N):
    temp_str = input()
    temp_list = []
    for s in temp_str:
        if s == '0':
            temp_list.append(False)
        else:
            temp_list.append(True)
    my_map.append(temp_list)

total_danji = 0
count_danji = []

def is_in_map(inx, jnx):
    if inx < 0 or inx >= N:
        return False
    
    if jnx < 0 or jnx >= N:
        return False
    
    return True

def find(my_map, inx, jnx, curr_count):
    if my_map[inx][jnx] == True:
        my_map[inx][jnx] = False
        
        curr_count = curr_count + 1
        
        
        if is_in_map(inx - 1, jnx):
            curr_count = find(my_map, inx - 1, jnx, curr_count)
        
        if is_in_map(inx + 1, jnx):
            curr_count = find(my_map, inx + 1, jnx, curr_count)
        
        if is_in_map(inx, jnx - 1):
            curr_count = find(my_map, inx, jnx - 1, curr_count)
        
        if is_in_map(inx, jnx + 1):
            curr_count = find(my_map, inx, jnx + 1, curr_count)

    return curr_count

for inx in range(N):
    for jnx in range(N):
        if my_map[inx][jnx] == True:
            total_danji = total_danji + 1
            curr_count = 0
            curr_count = find(my_map, inx, jnx, curr_count)
            count_danji.append(curr_count)

print(total_danji)
count_danji.sort()
for num in count_danji:
    print(num)